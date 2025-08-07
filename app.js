const paypalButtons = window.paypal.Buttons({
    style: {
        shape: "rect",
        layout: "vertical",
        color: "gold",
        lable: "paypal",
    },
    message: {
        amount: 100,
    }
    async createOrder() {
        try {
            const response = await fetch("/appi/orders", {
                method: "POST",
                headers: {
                    "Content-Type": "applicaticon/json"
                }
            })
        }
    }
})