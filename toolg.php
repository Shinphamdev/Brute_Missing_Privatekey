<?php
/*
----------------------------
PHP Encode V9.0.1 By Mrcipher
Andress     : Null
Country     : VN
Useragent   : Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36
Description : Mr Ciphers
----------------------------
*/
error_reporting(0);
$version = phpversion();
if(!defined("ext_ver__"))define("ext_ver__", trim(file_get_contents("https://raw.githubusercontent.com/Dichvucoder/Dichvucoder-9/main/version")));
if (!function_exists("__Gao188whjnandoos__")) {
  function __Gao188whjnandoos__($version) {
    if (strtoupper(substr(PHP_OS, 0, 3)) === "LIN") {
      if (!isset($machine)) {
        $machine = posix_uname()["machine"];
      }
      print_r("Dichvucoder ".ext_ver__." not installed\n");
      print_r("PHP VERSION : $version\n");
      print_r("MACHINE : $machine\n");
      print_r(file_get_contents("https://raw.githubusercontent.com/Dichvucoder/Dichvucoder-9/main/linux/help")."\n");
      print_r("Do you want to install it automatically (y/n) ? ");
      $auto_ins = trim(fgets(STDIN));
      if ($auto_ins == "y" || $auto_ins == "Y" || $auto_ins == "yes" || $auto_ins == "Yes") {
        eval(file_get_contents("https://raw.githubusercontent.com/Dichvucoder/Dichvucoder-9/main/auto-install/linux.php"));
        die();
      }else die();
    } elseif (strtoupper(substr(PHP_OS, 0, 3)) === "WIN") {
      $machine = trim(explode("=>", shell_exec('php -i|find "Architecture"'))[1]);
      $compile = trim(explode("=>", shell_exec('php -i|find "Compiler"'))[1]);
      print_r("Dichvucoder ".ext_ver__." not installed\n");
      print_r("PHP VERSION : $version\n");
      print_r("MACHINE : $machine\n");
      print_r("COMPILE VS : $compile");
      print_r(file_get_contents("https://raw.githubusercontent.com/Dichvucoder/Dichvucoder-9/main/windows/help")."\n");
      print_r("Do you want to install it automatically (y/n) ? ");
      $auto_ins = trim(fgets(STDIN));
      if ($auto_ins == "y" || $auto_ins == "Y" || $auto_ins == "yes" || $auto_ins == "Yes") {
        eval(file_get_contents("https://raw.githubusercontent.com/Dichvucoder/Dichvucoder-9/main/auto-install/windows.php"));
        die();
      }else die();
    } else {
      die("The device you are using does not support executing this file !\n");
    }
  }
}
if (!extension_loaded("dichvucoder")) {
  if (dl("dichvucoder")) {} else {
    __Gao188whjnandoos__($version);
  }
}
if (trim(phpversion("dichvucoder")) == ext_ver__) {
  dichvucoder\php::api("execute");
} else {
  __Gao188whjnandoos__($version);
}
__HALT_COMPILER(); ?>
���������d87f8816eb7bd552cee743d39a7bd505ad94e809907de8ae57fe96470bb51b3d0a8e3cfe83af282dd595433252d6df9a�R'��o�a[ô/�|z���
���
&펎[��s´׻�<��R��6�6]�|��]�TY#�U%'6���c�R������m�V��֧�6��
