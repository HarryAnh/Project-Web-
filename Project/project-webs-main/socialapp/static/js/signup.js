function kiemtra() {
    var loi = "";
    // kiểm tra tên đăng nhập : text + length 
    var tdn = document.getElementById("username");
        if(tdn.value==""){
            tdn.className="loi";        
            loi += "Tên đăng nhập không được bỏ trống<br>";
        }
        else if(tdn.value.length<=6){
            tdn.className="loi";       
            loi += "Tên đăng nhập quá ngắn<br>";        
        }
        else if(tdn.value.length>10){
            tdn.className="loi";       
            loi += "Tên đăng nhập quá dài<br>";        
        }
        else tdn.className="txt";  
    // kiểm tra mật khẩu : text + length 

    // kiểm tra họ tên : text

    //kiểm tra email

    //kiểm tra  phái : radio
 
    //kiểm tra sở thích : checkbox

    // kiểm tra nghề nghiệp : select
    
    // kiểm tra giới thiệu : textarea

    // trả về giá trị kiểm tra
    if(loi!=""){
        document.getElementById('baoloi').innerHTML="<p>" + loi + "</p>";
        return false;
    }
}
