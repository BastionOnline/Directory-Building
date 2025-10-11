document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")
    const scheduleBtn = document.getElementById("scheduleFileInput")
    const dateInput = document.getElementById("dateInput")
    const customDate = document.getElementById("customDate")

    const buildBtn = document.getElementById("build")

    customDate.checked = true;

    balanceBtn.addEventListener("click", async () => {
        try{
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

    scheduleBtn.addEventListener("click", async () => {
        try {
            const scheduleStat = window.pywebview.api.selectScheduleFile()
        } catch (error) {

        }
    })

    dateInput.addEventListener("change", async () => {
        try{
            // event listener works on html elements not strings or values
            const dateValue = dateInput.value // or valueAsDate
            
            const dateSet = await window.pywebview.api.dateSelection(dateValue)
            
            alert("value changed!")
        } catch (err) {
            alert("year selection error: ", err);
        }
    })

    buildBtn.addEventListener("click", async() => {
        try {
            const buildStat = window.pywebview.api.initializeBuildDirectory()
        } catch (error) {

        }
    })
    
    customDate.addEventListener("change", async () => {
        try {
            alert(customDate.checked)

            customDateChoice = customDate.checked;

            const customDateStatus = await window.pywebview.api.customizeDate(customDateChoice)

        } catch (err) {

        }
    })
    

})