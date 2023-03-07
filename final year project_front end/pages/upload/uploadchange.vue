<template>
	<view class="loginpage bg-white">


		<!--title-->
		<view style="padding-top: 20upx;">
			<view style="padding-bottom: 60upx;margin-left: 15upx;">
				<image @tap="gotomy()" src="../../static/icon/back.png" style="width: 60upx;height: 60upx;"></image>
			</view>
			<view class="title">
				<view
					style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
					①修改</view>
				<text class="login">個人信息</text>
			</view>
		</view>
		<view>
			<view class="info">
				<view style="margin-top: 15upx;margin-bottom: 15upx;">

					<text style="font-size: 35upx;color: #000000;">您的身份證賬號：</text>
					<text style="font-size: 35upx;color: #000000;">{{detail.bir_id}}</text>



				</view>
				<view style="margin-top: 15upx;margin-bottom: 15upx;">

					<text style="font-size: 35upx;color: #000000;">您的性別：</text>
					<text style="font-size: 35upx;color: #000000;">{{detail.sex}}</text>

				</view>
				<view style="margin-top: 15upx;margin-bottom: 15upx;">
					<text style="font-size: 35upx;color: #000000;">您的生日:</text>
					<text style="font-size: 35upx;color: #000000;">{{detail.birthday}}</text>
				</view>
				<view style="margin-top: 15upx;margin-bottom: 15upx;">
					<text style="font-size: 35upx;color: #000000;">您的姓名：</text>
					<text style="font-size: 35upx;color: #000000;">{{detail.name}}</text>
				</view>

			</view>

			<view style="margin-top: 20upx;">

				<view class="input-fa">
					<input class="log-input" :placeholder="'請在此修改身份證號碼'" v-model="form.edit_bir_id" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請在此修改性別'" v-model="form.edit_sex" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請在此修改生日日期'" v-model="form.edit_birthday" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請在此修改姓名'" v-model="form.edit_name" />
				</view>
			</view>
		</view>


		<view style="margin: 40upx;" class="flex justify-center">
			<button @tap="editidcard()" class="bg-gradual-blue round" style="width: 650upx;">
				確認修改
			</button>
		</view>
		<view class="title">
			<view
				style="font-size: 300%;font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;">
				②修改</view>
			<text class="login">參賽信息</text>
		</view>
		<view class="info">
			<view style="margin-top: 15upx;margin-bottom: 15upx;">

				<text style="font-size: 35upx;color: #000000;">您的隊伍編號：</text>
				<text style="font-size: 35upx;color: #000000;">{{team_detail.team_num}}</text>

				<view style="margin-top: 15upx;margin-bottom: 15upx;">
					<text style="font-size: 35upx;color: #000000;">您的隊伍類型：</text>
					<text style="font-size: 35upx;color: #000000;">{{team_detail.team_type}}</text>
				</view>

			</view>
			<view style="margin-top: 15upx;margin-bottom: 15upx;">

				<text style="font-size: 35upx;color: #000000;">您的帶隊老師：</text>
				<text style="font-size: 35upx;color: #000000;">{{team_detail.tutor}}</text>

			</view>
			<view style="margin-top: 15upx;margin-bottom: 15upx;">
				<text style="font-size: 35upx;color: #000000;">您的隊友:</text>
				<text style="font-size: 35upx;color: #000000;">{{team_detail.team_mem_two}}</text>
			</view>
			<view style="margin-top: 15upx;margin-bottom: 15upx;">
				<text style="font-size: 35upx;color: #000000;">您的另一位隊友：</text>
				<text style="font-size: 35upx;color: #000000;">{{team_detail.team_mem_three}}</text>
			</view>
			<view style="margin-top: 20upx;">
				<view class="input-fa">
					<input class="log-input" :placeholder="'請修改您的隊伍編號'" v-model="form.edit_team_num" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請修改您的隊伍類型'" v-model="form.edit_team_type" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請修改您帶隊老師的姓名'" v-model="form.edit_tutor" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請修改您隊友的姓名'" v-model="form.edit_team_mem_two" />
				</view>
				<view class="input-fa">
					<input class="log-input" :placeholder="'請修改您另一位隊友的姓名（如無則填無）'" v-model="form.edit_team_mem_three" />
				</view>

			</view>

			<view style="margin: 40upx;" class="flex justify-center">
				<button @tap="editteaminfo()" class="bg-gradual-blue round" style="width: 650upx;">
					確認修改
				</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {

			return {
				form: {
					edit_bir_id: "",
					edit_sex: "",
					edit_birthday: "",
					edit_name: "",
					edit_team_num: "",
					edit_tutor: "",
					edit_team_mem_two: "",
					edit_team_mem_three: "",
					edit_team_type: "",
				},


				detail: {

				},
				team_detail: {

				},

			}
		},
		methods: {
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

					},
				})
			},
			getteamdata() {
				uni.request({
					url: "http://127.0.0.1:5000/teamdetails",
					data: {
						id: this.uid
					},
					method: "GET",
					success: (res) => {
						this.team_detail = res.data.team_detail;
						console.log(this.team_detail);
					},
				})
			},

			editidcard(uid) {
				uni.request({
					url: "http://127.0.0.1:5000/editidcard",
					data: {
						edit_bir_id: this.form.edit_bir_id,
						edit_sex: this.form.edit_sex,
						edit_birthday: this.form.edit_birthday,
						edit_name: this.form.edit_name,
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: "修改成功"
						})
						uni.navigateBack({
							delta: 0,
						});
					}
				})
				//location.reload()
			},

			editteaminfo(uid) {
				uni.request({
					url: "http://127.0.0.1:5000/editteaminfo",
					data: {
						edit_team_num: this.form.edit_team_num,
						edit_tutor: this.form.edit_tutor,
						edit_team_mem_two: this.form.edit_team_mem_two,
						edit_team_mem_three: this.form.edit_team_mem_three,
						edit_team_type: this.form.edit_team_type,
					},
					method: "POST",
					success: (res) => {
						uni.showToast({
							icon: "none",
							title: "修改成功"
						})
						uni.navigateBack({
							delta: 0,
						});
					}
				})
				//location.reload()
			},
			gotomy() {
				uni.switchTab({
					url: "../my/my"
				})
			}
		},
		onLoad(options) {
			//this.goods_id = options.id;
			this.getdata()
			this.getteamdata()
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
</script>
<style>
	.loginpage {
		height: 1500upx;
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

	.info {
		padding-left: 50upx;
		padding-right: 50upx;
		margin-top: 70upx;
	}
</style>
