<template>
	<view class="loginpage bg-white" >
		<view style=" padding-top: 20upx;">
			<view style="padding-bottom: 60upx;margin-left: 15upx;">
				<image @tap="gotomy()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
			</view>
		</view>
		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				① 請</view>
			<text class="login">上傳參賽視頻</text>
		</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;color: red;"
			v-if="!isuploadvideo">未上傳</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;"
			v-if="isuploadvideo">已上傳</view>
		<view class="text"><text>中學組：參賽隊伍必須使用Alice 2.x</text><text style="color: red;">*</text><text>（2.4
				或以上）編程世界編寫一個與主題相關的動畫，作品的執行時間不應少於1分鐘，但不能超過3分鐘。</text></view>
		<view class="text"><text>公開組：參賽隊伍必須使用Alice 3.x</text><text style="color: red;">*</text><text>（3.5
				或以上），Blender或Unity編寫一個與主題相關的動畫，作品的執行時間不應少於2分鐘，但不能超過5分鐘。</text></view>
		<view class="text"><text>如作品的執行時間超出上述規定時間，將被扣減分數。</text></view>
		<view class="text"><text style="color: red;">*</text><text>視頻格式僅限.MP4。</text></view>
		<view class="text"><text style="color: red;">*</text><text>同支隊伍只需提交一次作品。</text></view>
		<view style="margin: 40upx;" class="flex justify-center">
			<button @click="uploadVideoFile" class="bg-gradual-blue round" style="width: 650upx;">
				上傳
			</button>
		</view>

		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				② 請</view>
			<text class="login">上傳參賽聲明書</text>
		</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;color: red;"
			v-if="!isuploadstatement">未上傳</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;"
			v-if="isuploadstatement">已上傳</view>
		<view class="text"><text style="color: red;">*</text><text>文檔格式僅限.doc或.docx。</text></view>
		<view class="text"><text style="color: red;">*</text><text>同支隊伍只需提交一次聲明書。</text></view>
		<view style="margin: 40upx;" class="flex justify-center">
			<button @click="uploadstatement" class="bg-gradual-blue round" style="width: 650upx;">
				上傳
			</button>
		</view>

		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				③ 請</view>
			<text class="login">上傳參賽作品說明書</text>
		</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;color: red;"
			v-if="!isuploadinstruction">未上傳</view>
		<view class="cu-tag bg-yellow sm radius status-logo" style="font-size: 16px;font-weight: bold;"
			v-if="isuploadinstruction">已上傳</view>
		<view class="text"><text style="color: red;">*</text><text>文檔格式僅限.doc或.docx。</text></view>
		<view class="text"><text style="color: red;">*</text><text>同支隊伍只需提交一次說明書。</text></view>
		<view style="margin: 40upx;" class="flex justify-center">
			<button @click="uploadinstruction" class="bg-gradual-blue round" style="width: 650upx;">
				上傳
			</button>
		</view>


	</view>
</template>

<script>
	export default {

		data() {

			return {
				form: {
					description: "",
				},
				textmsg: {
					title: '交件提醒',
					content: '請於2022年2月28日前將所需文件上傳至本頁，逾期不候',
					contentTwo: '',
					cancel: '取消',
					confirm: '確定'
				},
				isuploadvideo: false,
				isuploadinstruction: false,
				isuploadstatement: false,
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
						console.log(res.data);
						//console.log("Does he/she had uploaded video? " + this.detail.is_upload_video);
						if (this.detail.is_upload_video == "true"){
							this.isuploadvideo = true;
										
						}
						if (this.detail.is_upload_instruction == "true"){
							this.isuploadinstruction = true;

						}
						if (this.detail.is_upload_statement == "true"){
							this.isuploadstatement = true;

						}

					},
				})
			},
			uploadstatement() {
				uni.chooseFile({
					count: 1,
					extension: ['.docx', '.doc'],
					success: function(res) {
						console.log(res.tempFilePaths[0]);
						uni.uploadFile({
							url: "http://127.0.0.1:5000/uploadstatement",
							filePath: res.tempFilePaths[0], // uni.chooseImage函数调用后获取的本地文件路劲
							name: 'wordfile', //后端通过'file'获取上传的文件对象
							// header: {
							// 	"Content-Type": "multipart/form-data"
							// },
							success: (file) => {
								this.isuploadstatement = true;
								console.log(file.data);
								uni.showToast({
									title: '聲明書上傳成功',
									duration: 3000
								})
								uni.navigateBack({
									
								})
							}
						});
					}
				})
			},
			uploadinstruction() {
				uni.chooseFile({
					count: 1,
					extension: ['.docx', '.doc'],
					success: function(res) {
						console.log(res.tempFilePaths[0]);
						uni.uploadFile({
							url: "http://127.0.0.1:5000/uploadinstruction",
							filePath: res.tempFilePaths[0], // uni.chooseImage函数调用后获取的本地文件路劲
							name: 'wordfile', //后端通过'file'获取上传的文件对象
							// header: {
							// 	"Content-Type": "multipart/form-data"
							// },
							success: (file) => {
								this.isuploadinstruction = true;
								console.log(file.data);
								uni.showToast({
									title: '說明書上傳成功',
									duration: 3000
								})
								uni.navigateBack({
									
								})
							}
						});
					}
				})
			},
			uploadVideoFile() {
				uni.chooseVideo({
					count: 1,
					extension: ['.mp4'],
					success: function(res) {
						self.src = res.tempFilePath;
						console.log(self.src);
						uni.getVideoInfo({
							src: res.tempFilePath,
							success: function(video) {
								self.duration = video.duration;
								self.size = video.size;
								self.height = video.height;
								self.width = video.width;
								console.log(self.duration);
								console.log(video.size);
								console.log(video.height);
								console.log(video.width);
								if (self.duration < 300 && self.duration > 1) {
									uni.showToast({
										title: '作品上傳成功',
										duration: 3000
									})
									uni.uploadFile({
										url: "http://127.0.0.1:5000/uploadvideo", // 后端api接口
										filePath: self
											.src, // uni.chooseImage函数调用后获取的本地文件路劲
										name: 'video', //后端通过'file'获取上传的文件对象
										// 	formData: {

										// 	},
										success: (file) => {
											
											console.log(file.data);
								uni.navigateBack({
									
								})
										},

									});
								} else {
									uni.showToast({
										title: '作品規格不符合要求，請重新上傳',
										duration: 3000,

									})
								}
							},
						})



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
			// onShow() {
			// 	var userInfo = this.getGlobalUser("globalUser")

			// 	if (userInfo != null) {
			// 		// this.userIsLogin = true;
			// 		this.userInfo = userInfo;
			// 	} else {
			// 		// this.userIsLogin = false;
			// 		this.userInfo = {};
			// 	}
			// 	console.log(userInfo.uid);
			// },
			onLoad(options) {
				//this.goods_id = options.id;
				this.getdata();
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
		}
	}
</script>

<style>
	.status-logo {
		width: 130upx;
		height: 60upx;
	}

	.loginpage {
		height: 1200upx;
	}

	page {
		background-color: white;
	}

	.title {
		margin: 50upx;
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
		padding-left: 55upx;
		padding-right: 80upx;
		margin-top: 70upx;
	}

	.text {
		margin: 50upx;
		font-size: 120%;
		font-weight: bold;
		color: black;
	}
</style>
