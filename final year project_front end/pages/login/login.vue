<template>

	<view class="loginpage bg-white"">


		<!--title-->
		<view style=" padding-top: 20upx;">
		<view style="padding-bottom: 60upx;margin-left: 15upx;">
			<image @tap="gotomy()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
		</view>
		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				請</view>
			<text class="login">登錄</text>
		</view>
	</view>

	<!--input box-->
	<!-- 		<view class="input-fa">
			<view>
				用戶賬號：
			</view>
			<view>
				<input class="log-input" v-model="form.Userid" />
			</view>
			<view style="margin-top: 30upx;">
				用戶密碼：
			</view>
			<view>
				<input class="log-input" v-model="form.password" :password="true" />
			</view>
		</view> -->
	<view style="margin-top: 20upx;">
		<view class="input-fa">
			<input class="log-input" placeholder="用户賬號(電子郵箱)" v-model="form.email" />
		</view>
		<view class="input-fa flex align-center">
			<input class="log-input" :placeholder="'請輸入密碼'" v-model="form.password" :password="true" />
			<!-- <button :disabled="yzmclick" @tap="huoquyzm" class="cu-btn bg-orange" v-if="status==1">{{yzmtext}}</button> -->
		</view>
	</view>

	<!--login button-->
	<!-- 		<view style="margin-top: 80upx;" class="flex justify-center">
			<button @tap="login" class="bg-gradual-orange" style="width: 450upx;">
				Login
			</button>
		</view> -->
	<view style="margin-top: 40upx;" class="flex justify-center">
		<button @tap="login(form.Userid)" class="bg-gradual-blue round" style="width: 650upx;">
			登錄
		</button>
	</view>
	<!--change passwoed-->
	<!-- <view class="flex justify-center" style="margin-top: 15upx;">
			<text style="color:#b1b4b5;font-size: 90%;">Forget your password?</text>
		</view> -->

	<view class="flex justify-center" style="margin-top: 40upx;">
		<text @tap="register()" style="color:#06618c;font-size: 90%;">新用戶註冊</text>


	</view>
	<view class="flex justify-center" style="margin-top: 40upx;">
		<text @tap="forgetpassword()" style="color:#06618c;font-size: 90%;">忘記密碼?</text>
	</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					//Userid: "",
					email: "",
					password: "",
				},
				userIsLogin: false
			}
		},
		methods: {
			login(id) {
				uni.request({
					url: "http://127.0.0.1:5000/user/login",
					data: {
						//userid: this.form.Userid,
						email: this.form.email,
						password: this.form.password
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: res.data.desc,
						})
						if (res.data.status == 0) {
							var userInfo = res.data.info;
							console.log(userInfo);
							uni.setStorageSync("uid", res.data.userid);
							uni.setStorageSync("globalUser", userInfo);
							this.gotomy(this.form.Userid);

						}
					}
				})
			},
			gotohome() {
				uni.switchTab({
					url: "../index/index"
				})
			},
			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
			},
			gotoidmy(id) {
				uni.navigateTo({
					url: `http://127.0.0.1:5000/my/my?id=${id}`

				})

			},
			register() {
				uni.navigateTo({
					url: "../login/register"
				})
				
			},
			forgetpassword() {
				uni.navigateTo({
					url: "../login/forgetpassword"
				})
				
			}

		}
	}
</script>

<style>
	.loginpage {
		height: 1700upx;
	}

	.title {
		margin-left: 50upx;
	}

	.login {
		font-size: 250%;
		font-weight: bold;
		color: black;
	}

	.log-input {
		height: 100upx;
		border-bottom: 1upx solid #DDDDDD;
		flex-grow: 1;
	}

	.input-fa {
		padding-left: 50upx;
		padding-right: 50upx;
		margin-top: 50upx;
	}

	page {
		background-color: white;
	}
</style>
