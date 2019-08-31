<?php  
/** 
  * wechat php test 
  */  
  
//define your token
define("TOKEN", "loong");  
$wechatObj = new wechatCallbackapiTest();  
$wechatObj->valid();  
  
class wechatCallbackapiTest  
{  
    public function valid()  
    {
		echo "start..."
		
        $echoStr = $_GET["echostr"];  
  
        //valid signature , option  
        if($this->checkSignature()){  
            echo $echoStr;
            exit;  
        }  
    }  
          
    private function checkSignature()  
    {  
        $signature = $_GET["signature"];  
        $timestamp = $_GET["timestamp"];  
        $nonce = $_GET["nonce"];      
                  
        $token = TOKEN;  
        $tmpArr = array($token, $timestamp, $nonce);  
        sort($tmpArr);  
        $tmpStr = implode( $tmpArr );  
        $tmpStr = sha1( $tmpStr );  
          
        if( $tmpStr == $signature ){  
            return true;  
        }else{  
            return false;  
        }  
    }  
} 