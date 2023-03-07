<template>
	<view class="loginpage bg-white">

		<view style=" padding-top: 20upx;">
			<view style="padding-bottom: 60upx;margin-left: 15upx;">
				<image @tap="gotomy()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
			</view>

			<view class="title">
				<view
					style="font-size: 300%;font-family:'Lufcida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
					① 請上傳</view>
				<text class="login">身份證照</text>
			</view>
<!-- 			<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;color: red;"
				v-if="!isuploadedidcard">未上傳</view>
			<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;"
				v-if="isuploadedidcard">已上傳</view> -->
		</view>
		<view class="text"><text>報名需上傳身份證，成功識別後即為報名狀態，</text><text
				style="color: red;">*</text><text>但仍需您上傳參賽作品及資料。</text>
		</view>
		<view style="margin: 40upx;" class="flex justify-center">
			<button @click="uploadFile" class="bg-gradual-blue round" style="width: 650upx;">
				上傳圖片
			</button>
		</view>
		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lufcida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				② 請上傳</view>
			<text class="login">參賽信息</text>
		</view>
<!-- 		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;color: red;"
			v-if="!isuploadedteaminfo">未上傳</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;"
			v-if="isuploadedteaminfo">已上傳</view> -->
		<view class="text"><text
				style="color: red;">*</text><text>同支隊伍只需提交此表單一次,如您的隊友已填寫，則可跳過。</text>
		</view>
		
		<view class="input-fa">
			<input class="log-input" :placeholder="'請填寫您的組號'" v-model="form.team_num" />
		</view>
		<view class="input-fa">
			<input class="log-input" :placeholder="'請填寫您的導師名稱'" v-model="form.tutor" />
		</view>
		<view class="input-fa">
			<input class="log-input" :placeholder="'請填寫您的隊伍類型'" v-model="form.team_type" />
		</view>
		<view class="input-fa">
			<input class="log-input" :placeholder="'請填寫您的組員的姓名'" v-model="form.team_mem_two" />
		</view>
		<view class="input-fa">
			<input class="log-input" :placeholder="'請填寫您另一位組員的姓名（如無則填無）'" v-model="form.team_mem_three" />
		</view>
		<view style="margin: 40upx;" class="flex justify-center">
			<button @click="uploadteaminfo()" class="bg-gradual-blue round" style="width: 650upx;">
				上傳信息
			</button>
		</view>
	</view>

</template>

<script>
	export default {

		data() {

			return {
				form: {
					id: "",
					sex: "",
					birthday: "",
					userInfo: "",
					team_num: "",
					tutor: "",
					team_type: "",
					team_mem_two: "",
					team_mem_three: "",

				},
				isuploadedidcard: false,
				isuploadedteaminfo: false,
				test:"",
			}
		},
		methods: {
			uploadteaminfo(uid) {
					uni.request({
						url: "http://127.0.0.1:5000/uploadteaminfo",
						data: {
						team_num: this.form.team_num,
						tutor: this.form.tutor,
						team_type: this.form.team_type,
						team_mem_two: this.form.team_mem_two,
						team_mem_three: this.form.team_mem_three,
						},
						method: "POST",
						success: (res) => {
							uni.showToast({
								icon: "none",
								title: res.data.desc,
							})
							this.test = res.data.desc
							//this.isuploadedteaminfo = true;
							//uni.setStorageSync("isuploadedteaminfo", true);
							if (this.test == "參賽信息上传成功") {
								// uni.navigateTo({
								// 	url:"./upload/uploadchange"
								// });
								uni.navigateBack({
								
								});
							}

						},
						
					})
				



			},
			getdata() {
				uni.request({
					url: "http://127.0.0.1:5000/details",
					data: {
						id: this.uid
					},
					method: "GET",
					success: (res) => {
						this.detail = res.data.detail;
						console.log(res.data);
						//console.log(this.detail.bir_id);
						if (this.detail != null) {
							this.isuploadedidcard = true;

						}


					},
				})
			},
			getdteamdata() {
				uni.request({
					url: "http://127.0.0.1:5000/teamdetails",
					data: {
						id: this.uid
					},
					method: "GET",
					success: (res) => {
						this.detail = res.data.detail;
						console.log(res.data);
						//console.log(this.detail.bir_id);
						if (this.detail != null) {
							this.isuploadedteaminfo = true;
			
						}
			
			
					},
				})
			},
			uploadFile: function() {
				uni.chooseImage({
					count: 1,
					sizeType: ['original', 'compressed'],
					sourceType: ['album', 'camera'],
					success: function(res) {

						uni.previewImage({
							urls: res.tempFilePaths,

						})
						var tempFilePaths = res.tempFilePaths;
						var Proimgurl = res.tempFilePaths[0];
						uni.uploadFile({
							url: "http://127.0.0.1:5000/upload", // 后端api接口
							filePath: res.tempFilePaths[0], // uni.chooseImage函数调用后获取的本地文件路劲
							name: 'file', //后端通过'file'获取上传的文件对象
							formData: {
								// imgurl:res.tempFilePaths[0],

							},
							// header: {
							// 	"Content-Type": "multipart/form-data"
							// },
							success: (res) => {
								var arr = [];
								arr = res.data.split(",");
								console.log(arr[0]);
								console.log(arr[1]);
								console.log(arr[2]);
								console.log(arr[3]);
								console.log(arr[4]);
								console.log(arr[5]);
								uni.showToast({
									title: '識別成功並存儲',
									duration: 3000
								})
								uni.navigateBack({

								})
								//uni.setStorageSync("userIsRegistered", true);
							},
							fail: () => {
								uni.showToast({
									title: '識別失敗，請重新上傳',
									duration: 3000
								})
							}
						});


						;

					},
					fail: function(err) {
						console.log(err)
					}

				})
			},

			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
			},
			// onShow() {
			// 	var userInfo = this.getGlobalUser("globalUser")

			// 	if (userInfo != null) {
			// 		// this.userIsLogin = true;
			// 		this.userInfo = userInfo;
			// 	} else {
			// 		// this.userIsLogin = false;
			// 		this.userInfo = {};
			// 	}
			// console.log(userInfo.uid);
			// },
			onLoad(options) {
				this.getdata();
				this.getdteamdata();
				// var test = this.getTeamInfoUploadStatus("isuploadedteaminfo")
				// if (test != null) {
				// 	this.isuploadedteaminfo = true;
				// } else {

				// }
				
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
			getstatus(input) {

				uni.request({
					url: `http://127.0.0.1:5000/users/my?id=${input}`,
					method: "GET",
					success: (res) => {
						console.log(res.data)
						
					}
				})
			},

		}
	}
</script>

<style>
	.log-input {
		height: 70upx;
		border-bottom: 1upx solid #e7e7e7;
	}
	
	.input-fa {
		padding-left: 50upx;
		padding-right: 50upx;
		margin-top: 70upx;
	}
	.status-logo {
		width: 130upx;
		height: 60upx;
	}

	.loginpage {
		height: 2000upx;
	}

	page {
		background-color: white;
	}

	.title {
		margin: 50upx;
	}

	.text {
		margin: 50upx;
		font-size: 120%;
		font-weight: bold;
		color: black;
	}

	.login {
		font-size: 250%;
		font-weight: bold;
		color: black;
	}

	/* 	.log-input {
		height: 70upx;
		border-bottom: 1upx solid #e7e7e7;
	} */
	/* 
	.input-fa {
		padding-left: 55upx;
		padding-right: 80upx;
		margin-top: 70upx;
	} */
</style>
