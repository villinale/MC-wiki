//轮播
$(function(){
    // 初始化轮播
    $(".start-slide").click(function(){
        $("#myCarousel").carousel('cycle');
    });
    // 停止轮播
    $(".pause-slide").click(function(){
        $("#myCarousel").carousel('pause');
    });
    // 循环轮播到上一个项目
    $(".prev-slide").click(function(){
        $("#myCarousel").carousel('prev');
    });
    // 循环轮播到下一个项目
    $(".next-slide").click(function(){
        $("#myCarousel").carousel('next');
    });
    // 循环轮播到某个特定的帧 
    $(".slide-one").click(function(){
        $("#myCarousel").carousel(0);
    });
    $(".slide-two").click(function(){
        $("#myCarousel").carousel(1);
    });
    $(".slide-three").click(function(){
        $("#myCarousel").carousel(2);
    });
});


// 实现自动变成active同时取消其他active
function clickTab(node) {
    this_id.classList.add('active');
    for (const tab of document.getElementsByClassName('tab')) {
      if (tab.id !== node.id) {
        tab.classList.remove('active');
      }
    }
}

//自动生成代码
function spawn_item(node_id, self_node) {
    // 更改active状态
    clickTab(self_node);
    var fpath = "/static/mc_item/" + self_node.id + '/';//文件路径
    var insert_code = '';//要插入的代码
    var Photo_index = 0;
    var img_src;
    var prime;
    while (1)
    {
        img_src = fpath + Photo_index + ".png";
        prime = isExistFile(img_src);
        if (prime == 0) {
            break;
        }

        var target_path = ' target="item_introduce"';
        var href_path = ' href='+ 'mc_item/'+self_node.id+ '/'+ Photo_index;//暂时test
        insert_code += '<div style="float: left;">';
        insert_code += '<a class="item_sin col-md-1"'+href_path+target_path+'style="background-image: url(';
        insert_code +=  img_src + ');"></a>';
        insert_code += '</div > ';
        Photo_index++;
    }

    //插入代码
    node_id.innerHTML=insert_code;
}
//生成右侧介绍
//function spawn_introduce(){
//    //插入地址
//    var target = document.getElementByid("all_item_background");
//    //要擦入的代码
//    var insert_code ="";
////    插入代码
////    target.innerHTML
//}

// 判断文件是否存在
function isExistFile(url)  
{      
    var xmlHttp ;  
    if (window.ActiveXObject)  
    {  
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");  
    }  
    else if (window.XMLHttpRequest)  
    {  
        xmlHttp = new XMLHttpRequest();  
    }   
    xmlHttp.open("get",url,false);  
    xmlHttp.send();

    if (xmlHttp.readyState == 4) {
        if (xmlHttp.status == 200) {
            return true;//url存在                
        }
        else if (xmlHttp.status == 404)
            return false;//url不存在
        else
            return false;//其他状态
    }
    else
        return false;
    
}

// 单机回调函数
function clickTab(node) {
    node.classList.add('active');
    for (const tab of document.getElementsByClassName('Sidebar')) {
      if (tab.id !== node.id) {
        tab.classList.remove('active');
      }
    }
  }