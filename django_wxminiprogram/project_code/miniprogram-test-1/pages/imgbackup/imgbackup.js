// pages/imgbackup/imgbackup.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    needUploadFiles: [],
    downloadedBackupedFiles: []
  },

  chooseImage: function (e) {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          needUploadFiles: that.data.needUploadFiles.concat(res.tempFilePaths)
        });
      }
    })
  },

  previewImage: function (e) {
    wx.previewImage({
      current: e.currentTarget.id, // 当前显示图片的http链接
      urls: this.data.files // 需要预览的图片http链接列表
    })
  },

  uploadFiles: function(){
    for (var i = 0; i < this.data.needUploadFiles.length; i ++){
      var filePath = this.data.needUploadFiles[i]   // 迭代待上传文件列表，每一个都执行上传操作
      wx.uploadFile({
        url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/',
        filePath: filePath,
        name: 'test',
        success: function(res){
          console.log(res)
        }
      })
    }
  },

  downloadFiles: function(){
    var that = this
    wx.downloadFile({
      url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/' + 
        '?md5=' + 'f82228d940edbbb38a5e443da0748140',
      success: function(res) {
        var tempFile = res.tempFilePath
        var newDownloadedBackupedFiles = that.data.downloadedBackupedFiles
        newDownloadedBackupedFiles.push(tempFile)
        that.setData({
          downloadedBackupedFiles: newDownloadedBackupedFiles
        })
      }
    })
  },

  deleteFiles: function(){
    wx.request({
      url: app.globalData.serverUrl + app.globalData.apiVersion + 'service/image/' +
        '?md5=' + 'f82228d940edbbb38a5e443da0748140', // same url as the download url
      method: 'DELETE',
      success: function(res){
        console.log(res.data)
        wx.showToast({
          title: 'Delete success.',
        })
      }
    })
  },











  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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