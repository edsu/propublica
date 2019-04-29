from propublica import State, Representative

def test_get_reps():
    md = State("md")
    reps = md.get_representatives()
    assert len(reps) > 0

def test_get_bills():
    raskin = Representative("Jamie Raskin", id="R000606")
    bills = raskin.get_bills()
    assert len(bills) > 0
    bill = bills[0]
    assert bill.url.startswith('https://www.congress.gov')
