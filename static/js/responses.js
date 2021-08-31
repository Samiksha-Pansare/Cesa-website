function getBotResponse(input) {
    fetch('', {method: "POST", body: input}).then(results=>results.json()).then(console.log)
}
