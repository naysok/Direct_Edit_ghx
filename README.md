# Direct_Edit_ghx  


Grasshopper のネイティブファイルには、バイナリの .gh 形式と、Xml で定義された .ghx 形式がある。  
.ghx のほうは、文字列処理でゴリ押せばいろいろできるという説がある。  

ghx をななめ読みしたが、コンポーネントの定義が結構冗長で、カンバス上にあるコンポーネントに ID が振られていて（それはそう）コンポーネントの追加などを行うには真面目に解析が必要。  

狙ったものを取りに行くくらいならば簡単そうなので。手始めに Scrible へタイムスタンプの文字列でも追加したい。  

適当に書いた感想としては、Scrible 内の改行が、Xml の改行になるので非常につらい。クォーテーションで挟んで \n にして欲しい。。。  


### Syntax  

```xml
<!-- File Name -->
<item name="Name" type_name="gh_string" type_code="10">FINE_NAME (.ghx)</item>
<item name="Name" type_name="gh_string" type_code="10">Hello_World_rename.ghx</item>

<!-- Description -->
<!-- 改行はそのまま入るっぽい -->
<item name="Text" type_name="gh_string" type_code="10">TEXT</item>
<item name="Text" type_name="gh_string" type_code="10">Hello World!!</item>

```

