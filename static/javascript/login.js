$('#login-button').click(function(){
  $('#login-button').fadeOut("slow",function(){
    $("#container").fadeIn();
    TweenMax.from("#container", .4, { scale: 0, ease:Sine.easeInOut});
    TweenMax.to("#container", .4, { scale: 1, ease:Sine.easeInOut});
  });
});

$(".close-btn").click(function(){
  TweenMax.from("#container", .4, { scale: 1, ease:Sine.easeInOut});
  TweenMax.to("#container", .4, { left:"0px", scale: 0, ease:Sine.easeInOut});
  $("#container, #forgotten-container, #signup-container").fadeOut(800, function(){
    $("#login-button").fadeIn(800);
  });
});

/* Forgotten Password */
$('#forgotten').click(function(){
  $("#container").fadeOut(function(){
    $("#forgotten-container").fadeIn();
  });
});

/* Signup */
$('#signup').click(function(){
  $("#container").fadeOut(function(){
    $("#signup-container").fadeIn();
  });
});

$('#signup-button').click(function (){
  $.ajax("/UserManage/signup/",{
    type: "POST",
    dataType: "json",
    data: $('#signup-form').serialize(),
      success: function (result) {
        if(result.state == 'repeat_error'){
          alert("重复密码错误！");
        }
        if(result.state == 'user_exist'){
          alert("用户名已存在！");
        }
        if(result.state == 'success'){
          alert("注册成功！");
          $("#signup-container").fadeOut(function(){
            $("#container").fadeIn();
            });
        }
      },
    error : function() {
      alert("服务器异常，有人要扣工资了！");
    }
  });
});

$('#login').click(function (){
  $.ajax("/UserManage/login/",{
    type: "POST",
    dataType: "json",
    data: $('#login-form').serialize(),
      success: function (result) {
        if(result.state == 'not_exist_or_password_error'){
          alert("用户不存在或密码错误！");
        }
      },
    error : function() {
      alert("服务器异常，有人要扣工资了！");
    }
  });
});