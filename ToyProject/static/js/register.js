function password_check() {
  var pwCheck = document.userInfo;
  if (pwCheck.password.value != pwCheck.password2.value) {
    alert("비밀번호를 동일하게 입력하세요.");
    pwCheck.password.value = "";
    pwCheck.password2.value = "";
    event.preventDefault();
    return false;
  }

  var error = "이미 존재하는 아이디입니다.";
  if (error) {
    alert(error);
    return false;
  }

  return true;
}
