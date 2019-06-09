// pages/weather/weather.js
const app = getApp()
const popularCities = [
  {"province": "山东省", "city": "济南" }, 
  {"province": "湖南省", "city": "长沙" }, 
  {"province": "北京市", "city": "北京" },
  {"province": "上海市", "city": "上海" }]

Page({

  /**
   * 页面的初始数据
   */
  data: {
    isAuthorized: false,
    weatherData: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.updateWeatherData()
  },

  updateWeatherData: function(){
    var that = this
    wx.showLoading({
      title: 'loading',
    })
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/weather/',
      method: "POST",
      data: {
        cities: popularCities
      },
      success: function(res){
        var tempData = res.data.data
        that.setData({
          weatherData: tempData
        })
        wx.hideLoading()
      }
    })
  },








  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.updateWeatherData()
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})