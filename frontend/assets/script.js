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
    
    const customDateStatus = document.getElementById("customDateStatus")
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
        
        // dateInput.value = currentYear
        dateInput.value = nextYear
    }

    defaultYear()





    buildBtn.addEventListener("click", async() => {
        try {
            alert("Building...")
            // console.log("Building...")
            // filePropertySettings = [
            //     {"file": "Year",
            //         "setting": yearValue,
            //         // "api": () => window.pywebview.api.selectYear(),
            //         "status": yearStatus
            //     },
            //     {"file": "Customize Date",
            //         "setting": customDateSetting,
            //         // "api": () => window.pywebview.api.customizeDate(),
            //         "status": customDateStatus
            //     },
            //     {"file": "Balance",
            //         "setting": balanceStatus,
            //         // "api": () => window.pywebview.api.selectBalanceFile(),
            //         "status": balanceStatus
            //     },
            //     {"file": "Schedules",
            //         "setting": scheduleStatus,
            //         // "api": () => window.pywebview.api.selectScheduleFile(),
            //         "status": scheduleStatus
            //     },
            //     {"file": "Sales",
            //         "setting": salesStatus,
            //         // "api": () => window.pywebview.api.selectSalesFile(),
            //         "status": salesStatus
            //     },
            //     {"file": "Invoices",
            //         "setting": invoiceStatus,
            //         // "api": () => window.pywebview.api.selectInvoiceFile(),
            //         "status": invoiceStatus
            //     },
            //     {"file": "Hotel - Schedule",
            //         "setting": hotelStatus,
            //         // "api": () => window.pywebview.api.selectHotelFile(),
            //         "status": hotelStatus
            //     },
            //     {"file": "Destination Folder",
            //         "setting": destinationStatus,
            //         // "api": () => window.pywebview.api.selectDestinationFolder(),
            //         "status": destinationStatus
            //     }
            // ]

            // filePropertySettings = [
                                    // [["Balance"], [balanceStatus], [window.pywebview.api.selectBalanceFile()]]
                                    // [["Year"], [yearValue], [window.pywebview.api.selectYear()]]
                                    // [["Customize Date"], [customDateSetting], [window.pywebview.api.customizeDate()]]
                                    // [["Balance"], [balanceStatus], [window.pywebview.api.selectBalanceFile()]],
                                    // [["Schedules"], [scheduleStatus], [window.pywebview.api.selectScheduleFile()]],
                                    // [["Sales"], [salesStatus], [window.pywebview.api.selectSalesFile()]],
                                    // [["Invoices"], [invoiceStatus], [window.pywebview.api.selectInvoiceFile()]],
                                    // [["Hotel - Schedule"], [hotelStatus], [window.pywebview.api.selectHotelFile()]],
                                    // [["Destination Folder"], [destinationStatus], [window.pywebview.api.selectDestinationFolder()]]
                                    // ]
            alert("still building...")
            // alert(filePropertySettings[0][0][0])

            async function confirmJson(file, status, apiCall) {
            // for (const files of filePropertySettings) {
                const check = await window.pywebview.api.checkUserDefaults(file)
                if (check.bool === false) {
                    alert(`Please set up user defaults before building: ${file}`)

                    const updateFile = await apiCall
                    alert(updateFile)

                    const jsonFilePath = await window.pywebview.api.checkUserDefaults(file)
                    alert(jsonFilePath.value)

                    status.innerHTML = jsonFilePath.value
                }
            }

            confirmJson("Balance", balanceStatus, window.pywebview.api.selectBalanceFile())

            // const customDateCheck = await window.pywebview.api.checkUserDefaults("Customize Date")
            const balanceCheck = await window.pywebview.api.checkUserDefaults("Balance")
            alert(balanceCheck.bool)
            // if it is false, load prompt to set up defaults
            // def updateJson(fileProp, setting):

            if (balanceCheck.bool === false) {
                alert("Please set up user defaults before building")
                const updateBalance = await window.pywebview.api.selectBalanceFile()
                alert(updateBalance)
                const jsonBalanceFilePath = await window.pywebview.api.checkUserDefaults("Balance")
                alert(jsonBalanceFilePath.value)
                balanceStatus.innerHTML = jsonBalanceFilePath.value
            }

            // alert(userDefaultCheck.bool)


            // const jsonCustomizeDate = await check("Customize Date", customDateSetting)
            // const jsonBalance = await check("Balance", balanceStatus)
            // const jsonSchedules = await check("Schedules", scheduleStatus)
            // const jsonSales = await check("Sales", salesStatus)
            // const jsonInvoices = await check("Invoices", invoiceStatus)
            // const jsonHotel = await check("Hotel - Schedule", hotelStatus)
            // const jsonDestination = await check("Destination Folder", destinationStatus)

            // alert(jsonCustomizeDate)
            // alert(jsonBalance)
            // alert("test")
    
            // const buildStat = window.pywebview.api.initializeBuildDirectory()
        } catch (error) {

        }
    })
    
    customDate.addEventListener("change", async () => {
        try {
            // alert(customDate.checked)

            customDateChoice = customDate.checked;
            customDateSetting.innerHTML = customDateChoice
            

            const customDateSetting = await window.pywebview.api.customizeDate(customDateChoice)
            alert(customDateSetting.value)
            customDateStatus.innerHTML = customDateSetting.value


        } catch (err) {

        }
    })
        
    balanceBtn.addEventListener("click", async () => {
        try{
            const balanceFilePath = await window.pywebview.api.selectBalanceFile()
            // alert(balanceFilePath)
            balanceStatus.innerHTML = balanceFilePath

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
            const scheduleSetting = await window.pywebview.api.selectScheduleFile()
            // alert(scheduleSetting)
            scheduleStatus.innerHTML = scheduleSetting
        } catch (error) {

        }
    })

    saleBtn.addEventListener("click", async () => {
        try {
            const saleSetting = await window.pywebview.api.selectSalesFile()
            // alert(saleSetting)
            salesStatus.innerHTML = saleSetting
        } catch {

        }
    })

    invoiceBtn.addEventListener("click", async () => {
        try {
            const invoiceSetting = await window.pywebview.api.selectInvoiceFile()
            // alert(invoiceSetting)
            invoiceStatus.innerHTML = invoiceSetting
        } catch {

        }
    })    


    hotelBtn.addEventListener("click", async () => {
        try {
            const hotelSetting = await window.pywebview.api.selectHotelFile()
            // alert(hotelSetting)
            hotelStatus.innerHTML = hotelSetting
        } catch {

        }
    })

    destinationFolderBtn.addEventListener("click", async () => {
        try {
            const destinationSetting = await window.pywebview.api.selectDestinationFolder()
            // alert(destinationSetting)
            destinationStatus.innerHTML = destinationSetting
        } catch {

        }
    })    



    // async function check(fileProp, setting) {
    //     return new Promise((resolve, reject) => {
    //         window.addEventListener('pywebviewready', async () => {
    //             try {
    //                 const filePropStatus = await window.pywebview.api.loadUserDefaults(fileProp);
    //                 if (filePropStatus.bool === true) {
    //                     setting.innerHTML = filePropStatus.value;
    //                     resolve(filePropStatus.value);
    //                 } else {
    //                     setting.innerHTML = `❌ ${fileProp} needs to be set`;
    //                     resolve(null);
    //                 }
    //             } catch (err) {
    //                 alert(`Error loading default: ${err}`);
    //                 reject(err);
    //             }
    //         });
    //     });
    // }






    async function check(fileProp, setting) {
        window.addEventListener('pywebviewready', async () => {
            try {
                const filePropStatus = await window.pywebview.api.loadUserDefaults(fileProp);
                if (filePropStatus.bool === true) {
                    setting.innerHTML = filePropStatus.value
                    return "filePropStatus"

                } else {
                    setting.innerHTML = `❌ ${fileProp} needs to be set`
                    return "filePropStatus"
                }
            } catch (err) {
                alert(`Error loading default: ${err}`);
                // create needed key, value pair
            }
        })
    }

    check("Customize Date", customDateStatus)
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

function alertTest(test){
    alert(test)
}

function ring(){
    alert("ring")
}
   