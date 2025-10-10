document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")

    balanceBtn.addEventListener("click", async () => {
        try{
            alert("clicked")
            const balanceFilePath = await window.pywebview.api.selectBalanceFile()

            if (!balanceFilePath) {
                alert("Balance File not selected")
            } else {
                alert("Balance File Selected")
            }
        } catch (err) {
            alert("File selection failed:", err);
            // status.textContent = "❌ File selection failed.";
        }})

})