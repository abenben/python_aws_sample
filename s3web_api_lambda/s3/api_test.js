const send_message = () => {
    // URLを作成
    let input_label = document.getElementById("input_textfield");
    var parameter = input_label.value;
    parameter = parameter.replace(/\r?\n/g, '\\r\\n'); // 改行コードを入れるとAWSでの処理が怪しかったので、文字列に置換している（TODO:改善）
    parameter = encodeURI(parameter);
    console.log(parameter);

    request_url = "https://8f79ikpzm2.execute-api.ap-northeast-1.amazonaws.com/prod/hello?param1=";
    request_url = request_url + parameter;
    console.log(request_url);

    // リクエストオブジェクトの作成
    var request = new XMLHttpRequest();
    request.open('GET', request_url, true);
    // request.setRequestHeader("x-api-key", "0IZQK3k1tb3LhIgFRGWGDO5ZR5CqTFkEMCDMrn40");
    request.responseType = 'json';

    // リクエストが成功したときに呼ばれる関数
    request.onload = function () {
      var json_data = this.response;
      var return_message = json_data;
      // 結果をhtmlに表示する
      let output_label = document.getElementById("output_label");
      output_label.innerText = return_message
    };

    request.send(); // URLリクエストを送信する
}
