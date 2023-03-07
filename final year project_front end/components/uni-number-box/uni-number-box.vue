<template>
	<view class="uni-numbox">
		<view @click="_calcValue('minus')" class="uni-numbox__minus uni-cursor-point">
			<text class="uni-numbox--text" :class="{ 'uni-numbox--disabled': inputValue <= min || disabled }" style="color: #878686;border-radius: 10upx;" >-</text>
		</view>
		<input :disabled="disabled" @focus="_onFocus" @blur="_onBlur" class="uni-numbox__value" type="number" v-model="inputValue" style="color: #747373;"/>
		<view @click="_calcValue('plus')" class="uni-numbox__plus uni-cursor-point">
			<text class="uni-numbox--text" :class="{ 'uni-numbox--disabled': inputValue >= max || disabled }" style="color: #878686;">+</text>
		</view>
	</view>
</template>
<script>
	/**
	 * NumberBox 数字输入框
	 * @description 带加减按钮的数字输入框
	 * @tutorial https://ext.dcloud.net.cn/plugin?id=31
	 * @property {Number} value 输入框当前值
	 * @property {Number} min 最小值
	 * @property {Number} max 最大值
	 * @property {Number} step 每次点击改变的间隔大小
	 * @property {Boolean} disabled = [true|false] 是否为禁用状态
	 * @event {Function} change 输入框值改变时触发的事件，参数为输入框当前的 value
	 */

	export default {
		name: "UniNumberBox",
		props: {
			value: {
				type: [Number, String],
				default: 1
			},
			min: {
				type: Number,
				default: 0
			},
			max: {
				type: Number,
				default: 100
			},
			step: {
				type: Number,
				default: 1
			},
			disabled: {
				type: Boolean,
				default: false
			}
		},
		data() {
			return {
				inputValue: 0
			};
		},
		watch: {
			value(val) {
				this.inputValue = +val;
			},
			inputValue(newVal, oldVal) {
				if (+newVal !== +oldVal) {
					this.$emit("input", newVal);
					
						this.$emit("change", newVal);
				}
			}
		},
		created() {
			this.inputValue = +this.value;
		},
		methods: {
			_calcValue(type) {
				if (this.disabled) {
					return;
				}
				const scale = this._getDecimalScale();
				let value = this.inputValue * scale;
				let step = this.step * scale;
				if (type === "minus") {
					value -= step;
					if (value < (this.min * scale)) {
						return;
					}
					if (value > (this.max * scale)) {
						value = this.max * scale
					}
				} else if (type === "plus") {
					value += step;
					if (value > (this.max * scale)) {
						return;
					}
					if (value < (this.min * scale)) {
						value = this.min * scale
					}
				}

				this.inputValue = String(value / scale);
			},
			_getDecimalScale() {
				let scale = 1;
				// 浮点型
				if (~~this.step !== this.step) {
					scale = Math.pow(10, (this.step + "").split(".")[1].length);
				}
				return scale;
			},
			_onBlur(event) {
				this.$emit('blur', event)
				let value = event.detail.value;
				if (!value) {
					// this.inputValue = 0;
					return;
				}
				value = +value;
				if (value > this.max) {
					value = this.max;
				} else if (value < this.min) {
					value = this.min;
				}
				this.inputValue = value;
			},
			_onFocus(event) {
				this.$emit('focus', event)
			}
		}
	};
</script>
<style lang="scss" scoped>
	$box-height: 23px;
	/* #ifdef APP-NVUE */
	$box-line-height: 20px;
	/* #endif */
	$box-line-height: 16px;
	$box-width: 35px;

	.uni-numbox {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		height: $box-height;
		line-height: $box-height;
		width: 80px;
	}

	.uni-cursor-point {
		/* #ifdef H5 */
		cursor: pointer;
		/* #endif */
	}

	.uni-numbox__value {
		background-color: $uni-bg-color;
		width: 45px;
		height: $box-height;
		text-align: center;
		font-size: $uni-font-size-lg;
		border-width: 1rpx;
		border-style: solid;
		border-color: $uni-border-color;
		border-left-width: 1;
		border-right-width: 1;
	}

	.uni-numbox__minus {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
		justify-content: center;
		width: $box-width;
		height: $box-height;
		// line-height: $box-line-height;
		// text-align: center;
		font-size: 20px;
		color: $uni-text-color;
	//	background-color: #f9f9f9;
		border-width: 1rpx;
		border-style: solid;
		border-color: $uni-border-color;
		border-top-left-radius: 20rpx;
		border-bottom-left-radius: 20rpx;
		border-right-width: 0;
	}

	.uni-numbox__plus {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
		justify-content: center;
		width: $box-width;
		height: $box-height;
		border-width: 1rpx;
		border-style: solid;
		border-color: $uni-border-color;
		border-top-right-radius: 20rpx;
		border-bottom-right-radius: 20rpx;
		//background-color: #f9f9f9;
		border-left-width: 0;
	}

	.uni-numbox--text {
		font-size: 19px;
		color: $uni-text-color;
	}

	.uni-numbox--disabled {
		color: $uni-text-color-disable;
		/* #ifdef H5 */
		cursor: not-allowed;
		/* #endif */
	}
</style>
