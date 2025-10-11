document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")
    const scheduleBtn = document.getElementById("scheduleFileInput")
    const saleBtn = document.getElementById("saleFileInput")
    const invoiceBtn = document.getElementById("invoiceFileInput")
    const destinationFolderBtn = document.getElementById("destionationFolderInput")
    const hotelBtn = document.getElementById("hotelFileInput")    
    const dateInput = document.getElementById("dateInput")
    const customDate = document.getElementById("customDate")

    const buildBtn = document.getElementById("build")

    // customDate.checked = true;

    balanceBtn.addEventListener("click", async () => {
        try{
            const balanceFilePath = await window.pywebview.api.selectBalanceFile()

            // if (!balanceFilePath) {
            //     alert("Balance File not selected")
            // } else {
            //     alert("Balance File Selected")
            // }
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

    saleBtn.addEventListener("click", async () => {
        try {
            const saleStatus = window.pywebview.api.selectSalesFile()
        } catch {

        }
    })

    invoiceBtn.addEventListener("click", async () => {
        try {
            const invoiceStatus = window.pywebview.api.selectInvoiceFile()
        } catch {

        }
    })    

    destinationFolderBtn.addEventListener("click", async () => {
        try {
            const destinationStatus = window.pywebview.api.selectDestinationFolder()
        } catch {

        }
    })    

    hotelBtn.addEventListener("click", async () => {
        try {
            const hotelStatus = window.pywebview.api.selectHotelFile()
        } catch {

        }
    })

    dateInput.addEventListener("change", async () => {
        try{
            // event listener works on html elements not strings or values
            const dateValue = dateInput.value // or valueAsDate
            
            const dateSet = await window.pywebview.api.dateSelection(dateValue)
            
            // alert("value changed!")
        } catch (err) {
            // alert("year selection error: ", err);
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
            // alert(customDate.checked)

            customDateChoice = customDate.checked;

            const customDateStatus = await window.pywebview.api.customizeDate(customDateChoice)

        } catch (err) {

        }
    })
    

})