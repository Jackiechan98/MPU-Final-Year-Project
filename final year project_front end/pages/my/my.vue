<template>
</template>

<script>
</script>

<style>
</style>
<template>
	<view>
		<view class="flex justify-between  content1">

			<view class="flex">
				<view>
					<image v-if="userIsLogin" class="user-logo" src="../../static/client.jpg"></image>
				</view>
				<view style="margin-left: 20upx;">
					<view class="user-name" v-if="userIsLogin">
						<text>{{userInfo.uName}}</text>
						<view class="cu-tag bg-yellow sm radius" v-if="userIsRegistered">已報名</view>
						<view class="cu-tag bg-yellow sm radius" v-if="!userIsRegistered">未報名</view>
					</view>
					<view style="margin-top: 25upx;" v-if="userIsLogin">
						<!-- <view class="cu-tag round line-blue sm">{{userInfo.uid}}</view> -->
						<view class="cu-tag round line-blue sm">{{userInfo.email}}</view>
					</view>
				</view>
			</view>
			<view class="flex align-center" v-if="userIsLogin">
				<button class="cu-btn line-red round" @tap="logout()">
					<text class="text-red"></text>
					登出
				</button>
			</view>
			<view class="flex align-center" v-if="!userIsLogin">
				<button class="cu-btn line-red round" @tap="login()">
					<text class="text-red"></text>
					登入/注冊
				</button>
			</view>
		</view>
		<view style="margin-top: 2upx;" class="flex justify-center align-center flex-direction ">
			<view v-if="!userIsLogin" class="text"><text>請先登錄/註冊再使用本系統</text></view>
		</view>
		<view class="list-content" v-if="userIsLogin">
			<view @tap="gopage(i)" class="bg-white list-item" v-for="(p,i) in lists" :key="i">
				<text style="font-size: 130%;margin-right: 10upx;" :class="p.icon"></text><text>{{p.text}}</text>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				status: [],
				//user_id: "",
				userIsLogin: false,
				userIsRegistered: false,
				userInfo: "",
				lists: [{
						text: '報名參賽',
						icon: 'cuIcon-profile text-orange',

						url: "../upload/upload"

					},
					{
						text: "修改身份信息及參賽信息",
						icon: 'cuIcon-write text-black',
						url: "../upload/uploadchange"
					},
					{
						text: "上傳參賽作品",
						icon: "cuIcon-pullup text-brown",
						url: "../upload/uploadvideo"
					},

					{
						text: "修改密碼",
						icon: "cuIcon-writefill text-black",
						url: "../login/changepassword"
					},
					// {
					// 	text:"系统设置",
					// 	icon:"cuIcon-settingsfill text-cyan"
					// },{
					// 	text:"注销登录",
					// 	icon:"cuIcon-roundclosefill text-red",
					// 	url:"../login/login"
					// }
				]
			}
		},
		methods: {
			getdata() {
				uni.request({
					url: "http://127.0.0.1:5000/details",
					data: {
						id: this.uid
					},
					method: "GET",
					success: (res) => {
						this.detail = res.data.detail;
						console.log(this.detail);
						if (this.detail != null) {
							this.userIsRegistered = true;
						}

					},
					// fail: () => {

					// }
				})
			},
			upload() {
				uni.reLaunch({
					url: "../upload/upload"
				})
			},
			gotoidcardchange() {
				uni.reLaunch({
					url: "../upload/uploadchange"
				})
			},
			gotouploadvideo() {
				uni.reLaunch({
					url: "../upload/uploadvideo"
				})
			},
			gopage(item) {
				var url = this.lists[item].url;
				if (url != null && url != undefined) {
					uni.reLaunch({
						url: url
					});
				}
			},
			gotochange() {
				uni.navigateTo({
					url: "../login/changepassword"
				})
			},
			login() {
				uni.reLaunch({
					url: "../login/login"
				})
			},
			logout() {
				var globalUser = this.getGlobalUser("globalUser")
				uni.removeStorageSync("globalUser")
				// uni.redirectTo({
				// 	url: "../my/my"
				// })
				uni.navigateBack({

				})
				// uni.navigateTo({
				// url: "../my/my"
				// })
				//this.$forceUpdate()
			},

			onLoad(options) {

				var userInfo = this.getGlobalUser("globalUser")
				if (userInfo != null) {
					this.userIsLogin = true;
					this.userInfo = userInfo;
					this.getstatus(userInfo.email);
					this.getdata()
				} else {
					this.userIsLogin = false;
					this.userInfo = {};
				}

			},
			getstatus(input) {
				uni.request({
					url: `http://127.0.0.1:5000/users/my?id=${input}`,
					method: "GET",
					success: (res) => {
						console.log(res.data)
						// this.$forceUpdate()
					}
				})
			},
		}
	}
</script>

<style>
	.user-logo {
		width: 120upx;
		height: 120upx;
	}

	.content1 {
		padding: 30upx 30upx 30upx 30upx;
		background-color: #F8F8F8;
	}

	.user-name {
		font-size: 130%;
		display: flex;
		align-items: center;


	}

	/* 	.yueka-fa {
		background-color: #F8F8F8;
		display: flex;
		justify-content: center;
	} */

	/* 	.yueka {
		width: 600upx;
		height: 80upx;
		background-color: #FADBD9;
		border-top-left-radius: 18upx;
		border-top-right-radius: 18upx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		color: rgb(187, 50, 52);
		padding-left: 20upx;
		padding-right: 20upx;

	} */

	.list-item {
		height: 100upx;
		display: flex;
		align-items: center;
		padding-left: 40upx;
		padding-right: 20upx;
		border-bottom: 1upx #ddd solid;
	}

	.list-content {
		margin-top: 20upx;
	}

	.text {
		margin: 50upx;
		font-size: 120%;
		font-weight: bold;
		color: #8799A3;
	}
</style>
