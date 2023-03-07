import Vue from 'vue'
import App from './App'


Vue.config.productionTip = false
Vue.prototype.$url="http://127.0.0.1:5000"

// Vue.prototype.getTeamInfoUploadStatus = function(key) {
// 	var test = uni.getStorageSync("isuploadedteaminfo")
// 	if(test!=null&&test!=""&&test!=undefined){
// 		return test;
// 	}else{
// 		return null;
// 	}
// }

Vue.prototype.getGlobalUser = function(key) {
	var userInfo = uni.getStorageSync("globalUser")
	if(userInfo!=null&&userInfo!=""&&userInfo!=undefined){
		return userInfo;
	}else{
		return null;
	}
}
// Vue.prototype.getsearch_result = function(key) {
// 	var goodsInfo = uni.getStorageSync("search_result")
// 	if(goodsInfo!=null&&goodsInfo!=""&&goodsInfo!=undefined){
// 		return goodsInfo;
// 	}else{
// 		return null;
// 	}
// }

App.mpType = 'app'


const app = new Vue({
    ...App
})
app.$mount()