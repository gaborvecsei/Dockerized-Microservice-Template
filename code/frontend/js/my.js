$(document).ready(function () {
    $("#buttonPredict").click(function (event) {
        event.preventDefault();


        // Get the values from the input fields
        var userApiKey = document.getElementById("apiKeyInput").value;
        var numberOfChars = document.getElementById("numberOfCharsInput").value;

        // Reset input fields but the API Key filed (So we don't have to fill it again)
        document.getElementById("numberOfCharsInput").value = "";

        // Show waiting Modal
        changeResultModal("Waiting...", "This may take a few moments");
        $("#resultsModal").modal();

        // Send Request
        var result = sendServiceRequest(userApiKey, numberOfChars);

        result.done(function (data) {
            console.log(data);
            var results = data["service_result"];
            changeResultModal("Results", results);
        });
        result.fail(function (data) {
            console.log(data);
            var statusResponse = "";
            try {
                statusResponse = data["status"] + ": " + data.responseJSON["message"];
            } catch (err) {
                statusResponse = err;
            }
            changeResultModal("Failed", statusResponse);
        });
    });
});

function sendServiceRequest(apiKey, size) {
    var url = "http://localhost:8080/microservice/sample_service";
    var requestBody = JSON.stringify({api_key: apiKey, size: size});

    var request = $.ajax({
        type: 'POST',
        url: url,
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        data: requestBody
    });

    return request
}

function changeResultModal(title, message) {
    $("#resultModalTitle").empty().append(title);
    $("#resultModalServiceResult").empty().append(message);
}