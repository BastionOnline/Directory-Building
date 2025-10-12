document.addEventListener("DOMContentLoaded", async () => {
    const balanceBtn = document.getElementById("balanceFileInput")
    const scheduleBtn = document.getElementById("scheduleFileInput")
    const saleBtn = document.getElementById("saleFileInput")
    const invoiceBtn = document.getElementById("invoiceFileInput")
    const destinationFolderBtn = document.getElementById("destinationFolderInput")
    const hotelBtn = document.getElementById("hotelFileInput")    
    const dateInput = document.getElementById("dateInput")
    const customDate = document.getElementById("customDate")
    const progressBar = document.getElementById("progressBar")
    const buildBtn = document.getElementById("build")
    const customDateSetting = document.getElementById("customDateSetting")
    
    const progressStatus = document.getElementById("progressStatus")
    const balanceStatus = document.getElementById("balanceStatus")
    const scheduleStatus = document.getElementById("scheduleStatus")
    const salesStatus = document.getElementById("salesStatus")
    const invoiceStatus = document.getElementById("invoiceStatus")
    const hotelStatus = document.getElementById("hotelStatus")
    const destinationStatus = document.getElementById("destinationStatus")
    
    
    let customDateChoice = false;

    customDate.checked = true;
        // customDate.click

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
   

    // calc defatult year
    function defaultYear(){
        const currentDate = new Date();
        let currentYear = currentDate.getFullYear();
        let nextYear = currentYear + 1;
        
        dateInput.value = nextYear
    }

    defaultYear()


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


    hotelBtn.addEventListener("click", async () => {
        try {
            const hotelStatus = window.pywebview.api.selectHotelFile()
        } catch {

        }
    })

    destinationFolderBtn.addEventListener("click", async () => {
        try {
            const destinationStatus = window.pywebview.api.selectDestinationFolder()
        } catch {

        }
    })    

    async function check(fileProp, setting) {
        window.addEventListener('pywebviewready', async () => {
            try {
                const filePropStatus = await window.pywebview.api.loadUserDefaults(fileProp);
                alert(filePropStatus)
                // alert(PyValue.location)
                if (filePropStatus.value === true) {
                    // alert(`✅ ${jsonValue} found!`);
                    setting.innerHTML = filePropStatus

                } else {
                    setting.innerHTML = `❌ ${fileProp} needs to be set`
                    // alert(`❌ ${jsonValue} needs to be set`);
                    // const updatedValue = await window.pywebview.api.chooseDefault(jsonValue);
                    alert(updatedValue)
                }
            } catch (err) {
                alert(`Error loading default:`, err);
                // create needed key, value pair
            }
        })
    }

    check("Balance", balanceStatus)
    check("Schedules", scheduleStatus)
    check("Sales", salesStatus)
    check("Invoices", invoiceStatus)
    check("Hotel - Schedule", hotelStatus)
    check("Destination Folder", destinationStatus)

})

// Functions callable from Python
// These functions are called from Python using window.evaluate_js('functionName(args)')    

function handleProgress(data){
    progressBar.value = data.progressValue
    progressStatus.innerHTML = value.progressDescription
}

function updateProgress(value){
    progressBar.value = value
}

function progressStatusUpdate(value){
    progressStatus.innerHTML = value
}

function alertTest(){
    alert("test")
}

function ring(){
    alert("ring")
}
   