<template>
	<view class="loginpage bg-white">


		<!--title-->
		<view style="padding-top: 20upx;">
			<view style="padding-bottom: 60upx;margin-left: 15upx;">
				<image  @tap="gotomy()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
			</view>
			<view class="title">
				<view
					style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
					重設</view>
				<text class="login">密碼</text>
			</view>
		</view>



		<view style="margin-top: 20upx;">
			<view class="input-fa">
				<input class="log-input" :placeholder="'用戶郵箱'" v-model="form.email" />
			</view>
			<view style="margin: 40upx;" class="flex justify-center">
				<button @tap="sendmail" class="bg-gradual-blue round" style="width: 650upx;">
					發送驗證碼
				</button>
			</view>
			<view class="input-fa">
				<input class="log-input" :placeholder="'驗證碼'" v-model="form.code" />
			</view>
			<view class="input-fa">
				<input class="log-input" placeholder="請輸入新密碼" v-model="form.newpassword" :password="true"/>
			</view>
			<view class="input-fa">
				<input class="log-input" placeholder="請再次輸入新密碼" v-model="form.confirmnewpassword" :password="true"/>
			</view>
		</view>



		<view style="margin: 40upx;" class="flex justify-center">
			<button @tap="changepassword()" class="bg-gradual-blue round" style="width: 650upx;">
				確認修改
			</button>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				form: {
					
					newpassword: "",
					confirmnewpassword: "",
					code:"",
				}
			}
		},
		methods: {
			sendmail(){
			
				uni.request({
					url: "http://127.0.0.1:5000/sendforget",
					data: {
						email: this.form.email
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: res.data
						})
						console.log(res.data)
					}
				})
			},
			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
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
			
			onLoad(options) {
				var userInfo = this.getGlobalUser("globalUser")
				if (userInfo != null) {
					this.userIsLogin = true;
					this.userInfo = userInfo;
					this.getstatus(userInfo.email);
				} else {
					this.userIsLogin = false;
					this.userInfo = {};
				}
			},
			
			changepassword() {
				uni.request({
					url: "http://127.0.0.1:5000/user/forgetpw",
					data: {
						newpassword: this.form.newpassword,
						confirmnewpassword: this.form.confirmnewpassword,
						email:this.form.email,
						code:this.form.code,
						
					},
					method: "POST",
					success: (res) => {
						if (res.data.status == 0) {
							var userInfo = res.data;
							console.log(userInfo);
							uni.setStorageSync("uid", res.data.userid);
							uni.setStorageSync("globalUser", userInfo);
							uni.showToast({
								icon: "none",
								title: res.data.desc
							})
							uni.switchTab({
								url: "../my/my"
							})
						}
					}
				})
			}
		}
	}
</script>

<style>
	.loginpage {
		height: 1200upx;
	}

	page {
		background-color: white;
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
		height: 70upx;
		border-bottom: 1upx solid #e7e7e7;
	}

	.input-fa {
		padding-left: 50upx;
		padding-right: 50upx;
		margin-top: 70upx;
	}
</style>
