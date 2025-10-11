document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")
    const scheduleBtn = document.getElementById("scheduleFileInput")
    const saleBtn = document.getElementById("saleFileInput")
    const invoiceBtn = document.getElementById("invoiceFileInput")
    const destinationFolderBtn = document.getElementById("destinationFolderInput")
    const hotelBtn = document.getElementById("hotelFileInput")    
    const dateInput = document.getElementById("dateInput")
    const customDate = document.getElementById("customDate")
    const buildProgress = document.getElementById("buildProgress")
    const buildBtn = document.getElementById("build")
    const customDateSetting = document.getElementById("customDateSetting")

    customDate.checked = true;

    // Need to set it up for when pywebviewready
    // adding table element made it unmodular

    dateInput.addEventListener("change", async () => {
        try{
            // alert("value changed!")

            // event listener works on html elements not strings or values
            const dateValue = dateInput.value // or valueAsDate
            // alert(dateValue)
            const dateSet = await window.pywebview.api.dateSelection(dateValue)
            
            
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
    

    function updateProgress(value){
        buildProgress.value = value
    }

    customDate.addEventListener("change", async () => {
        try {
            alert(customDate.checked)

            customDateChoice = customDate.checked;
            customDateSetting.innerHTML = customDateChoice
            

            const customDateStatus = await window.pywebview.api.customizeDate(customDateChoice)

        } catch (err) {

        }
    })
    
    
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


})