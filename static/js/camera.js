var canvas
var ctx
var video;
var webcamWidth;
var webcamHeight;

navigator.getUserMedia = (
  navigator.getUserMedia ||
  navigator.webkitGetUserMedia ||
  navigator.mozGetUserMedia ||
  navigator.msGetUserMedia
);

video = document.querySelector("#videoElement");
canvas = document.getElementById("myCanvas")
ctx = canvas.getContext('2d')

function camera(){
  if (navigator.mediaDevices.getUserMedia) {
    let constraints = { 
      audio: false, 
      video: {
        width: { min: 400, ideal: 400, max: 400 },
        height: { min: 400, ideal: 400, max: 400 },
    }
      
  };
      navigator.mediaDevices.getUserMedia(constraints)
        .then(function (stream) {
          video.srcObject = stream;
          webcamWidth = stream.getVideoTracks()[0].getSettings().width
          webcamHeight = stream.getVideoTracks()[0].getSettings().height
          canvas.setAttribute('width', 420);
          canvas.setAttribute('height', 420);
        })
        .catch(function (error) {
          console.log(error,"Something went wrong!");
        });
    }
}

function getCurrentFrame() {
  ctx.drawImage(video, 0,0)
  img_dataURI = canvas.toDataURL('image/png')
  video.style.display = "none";
  document.getElementById("my-data-uri").src = img_dataURI

}

function recapture(){
  location.reload();
  // document.getElementById("my-data-uri").style.display='none';
  // video.style.display = "block";
}

function postData(){
  canvas.toDataURL('image/png')
  var reader = new FileReader();
  reader.onload = function(event) {
    var form = document.getElementById("myForm");
    var imageInput = document.getElementById("myImageInput");
    imageInput.value = canvas.toDataURL('image/png');
    form.submit();
  }
}

camera();
