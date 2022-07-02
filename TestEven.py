from checkpassword import CheckPassWord

def test_checkpassword_Tc_all_Pass_test():
     pw ='Phu0ng@123'
     assert (CheckPassWord.checkPassWord(pw))== True

def test_checkpassword_Tc_NOT_include_upper():
    pw = 'phu0ng@123'
    assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_NOT_include_lower():
    pw = 'PHU0NG@123'
    assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_check_len():
    pw = 'Phu0ng@'
    assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_NOT_include_number():
    pw = 'Phu0ngDoan@'
    assert (CheckPassWord.checkPassWord(pw))== True

def test_checkpassword_Tc_include_number_and_specail_char():
   pw = '123344!@#$%^&&**()'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_all_specail_char_and_len():
   pw = '!@#$%^&&**()'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_all_specail_char_and_not_len():
   pw = '!@#$%)'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_specail_char_and_upper_lower():
   pw = 'Phuong@'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_NOT_include_special_char():
   pw = 'Phu0ng123'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_all_upper_and_not_len():
   pw = 'PHUONG'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tcs_include_upper_and_len():
   pw = 'MYPHUONG'
   assert (CheckPassWord.checkPassWord(pw))== False 

def test_checkpassword_Tc_include_upper_and_number_and_lower():
   pw = 'Phuong123'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_include_lower_and_not_len():
   pw = 'phuong'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_include_lower_and_len():
   pw = 'myphuong'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_include_lower_and_number_and_len():
   pw = 'phuong1234'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_include_lower_and_number_and_not_len():
   pw = 'my1234'
   assert (CheckPassWord.checkPassWord(pw))== False

def test_checkpassword_Tc_include_number_and_special_char_and_not_len():
   pw = '1&&**()'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_lower_and_special_char_and_len():
   pw = 'phuong!@#'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_lower_and_special_char_and_not_len():
   pw = 'my!@#'
   assert (CheckPassWord.checkPassWord(pw))== False 

def test_checkpassword_Tc_include_special_char_and_len_and_upper():
   pw = 'PHUONG!@#'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_special_char_and_not_len_and_upper():
   pw = 'MY!@#'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_number_and_len_and_upper():
   pw = 'PHUONG123'
   assert (CheckPassWord.checkPassWord(pw))== False  

def test_checkpassword_Tc_include_number_and_not_len_and_upper():
   pw = 'MY123'
   assert (CheckPassWord.checkPassWord(pw))== False  