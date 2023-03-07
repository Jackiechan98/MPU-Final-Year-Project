<template>
	<view class="loginpage bg-white">


		<!--title-->
		<view style="padding-top: 20upx;">
			<view  style="padding-bottom: 60upx;margin-left: 15upx;">
				<image @tap="gotohome()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
			</view>
			<view class="title">
				<view
					style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
					請</view>
				<text class="login">註冊</text>
			</view>
		</view>

		<view style="margin-top: 20upx;">
			<view class="input-fa">
				<input  class="log-input" placeholder="自定義用户賬號" v-model="form.Userid" />
			</view>
			<view class="input-fa">
				<input  class="log-input" placeholder="您的姓名" v-model="form.username" />
			</view>
			<view class="input-fa flex align-center">
				<input class="log-input" :placeholder="'請输入密码'" v-model="form.Password" :password="true" />
			</view>
			<view class="input-fa flex align-center">
				<input class="log-input" :placeholder="'請再次输入密码'" v-model="form.ConfirmPassword" :password="true" />
			</view>

			<view class="input-fa">
				<input  class="log-input" placeholder="您的手机號碼" v-model="form.utel" />
			</view>
			<view class="input-fa">
				<input  class="log-input" placeholder="您的電子郵箱(將作為賬號登陸使用)" v-model="form.email" />
			</view>
			<view class="input-fa">
				<input  class="log-input" placeholder="驗證碼" v-model="form.code" />
			</view>
			<view style="margin: 40upx;" class="flex justify-center">
				<button @tap="sendmail()" class="bg-gradual-blue round" style="width: 650upx;">
					發送驗證碼
				</button>
			</view>

<!-- 			<view class="input-fa">
				<input  class="log-input" placeholder="您的住址" v-model="form.uAddress" />
			</view> -->
		</view>



	<view style="margin: 40upx;" class="flex justify-center">
		<button @tap="Register()" class="bg-gradual-blue round" style="width: 650upx;">
			註冊
		</button>
	</view>

	</view>
</template>

<script>
	export default {

		data() {


			return {
				form: {
					Userid: "",
					password: "",
					ConfirmPassword: "",
					// address: "",
					email: "",
					utel:"",
					username: "",
					code:"",
				},

			}
		},
		methods: {
			
			
			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
			},
			sendmail(){

				uni.request({
					url: "http://127.0.0.1:5000/send",
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
			gotohome() {
				uni.navigateTo({
					url: "../login/login"
				})
				
			},
			Register() {
				uni.request({
					url: "http://127.0.0.1:5000/user/register",
					data: {
						userid: this.form.Userid,
						password: this.form.Password,
						confirmPassword: this.form.ConfirmPassword,
						// address: this.form.uAddress,
						username: this.form.username,
						utel:this.form.utel,
						email: this.form.email,
						code: this.form.code,
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: res.data.desc
						})
						console.log(res.data)
						if (res.data.status == 0) {
							var userInfo = res.data
							console.log(userInfo.uName)
							uni.setStorageSync("uid", res.data.userid)
							uni.setStorageSync("globalUser", userInfo)
							this.gotomy();
							// uni.switchTab({
							// 	url: "../my/my"
							// })
						}
					}
				})
			}
		}
	}
</script>

<style>
	.loginpage {
		height: 1700upx;
	}

	page {
		background-color: white;
	}
	
	.log-input{
		height: 100upx;
		border-bottom: 1upx solid #DDDDDD;
		flex-grow: 1;
	}

	.title {
		margin-left: 50upx;
	}

	.login {
		font-size: 250%;
		font-weight: bold;
		color: black;
	}
	.input-fa {
		padding-left: 55upx;
		padding-right: 80upx;
		margin-top: 70upx;
	}
</style>
