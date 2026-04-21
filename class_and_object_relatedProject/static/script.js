async function addData() {
    const amount = document.getElementById('amount').value;
    const desc = document.getElementById('desc').value;
    const type = document.getElementById('type').value;

    await fetch('/add', {
        method: 'POST',
        headers: {'Content-Type' : 'application/json'},
        body: JSON.stringify({amount, desc, type})
    });

    loadSummary();
}

async function loadSummary() {
    const res = await fetch('/summary');
    const data = await res.json();

    document.getElementById('income').innerText = data.income;
    document.getElementById('expense').innerText = data.expense;
    document.getElementById('balance').innerText = data.balance;    
}

loadSummary();