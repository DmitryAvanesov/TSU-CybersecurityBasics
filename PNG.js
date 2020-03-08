var pngitxt = require('png-itxt');
var fs = require('fs');

fs.createReadStream('PNG-SOURCE.png')
  .pipe(pngitxt.get(function (err, data) {
    if (!err && data) {
      console.log(data.keyword, ":", data.value)
    }
  }))