from pages.login import Login
def test_valid_login(page):
    login = Login(page)
    login.Login("Admin", "admin123")
    assert "dashboard" in page.url
    
def test_invalid_login(page):
    login = Login(page)
    login.Login("Admin", "admin1234")
    assert "dashboard"  in page.url
    
def test_invalid_login1(page):
    login = Login(page)
    login.Login("Admin1", "ADMIN123")
    assert "dashboard"  in page.url
    
def test_invalid_login2(page):
    login = Login(page)
    login.Login("ADMIN", "ADMIN123")
    assert "dashboard"  in page.url
def test_invalid_login3(page):
    login = Login(page)
    login.Login("", "")
    assert "dashboard"  in page.url
    
def test_invalid_login4(page):
    login = Login(page)
    login.Login("Admin", "")
    assert "dashboard"  in page.url
def test_invalid_login5(page):
    login = Login(page)
    login.Login("", "admin123")
    assert "dashboard"  in page.url # dont use assertion in the pages folder.