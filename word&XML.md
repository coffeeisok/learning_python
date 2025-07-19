# word&XML

### word文档的本质是XML

* Word 文档（`.docx`）实际上是一个压缩文件，内部包含多个 XML 文件，用于存储文本、表格、样式等内容。例如：
  * `document.xml`：存储文档的主要内容
  * `styles.xml`：存储文档的样式信息
  * 其他 XML 文件存储图片、关系等



### XML结构与遍历

* Word文档的XML结构类似于：

``````xml
<w:document>
  <w:body>
    <w:p>标题段落1</w:p>
    <w:p>标题段落2</w:p>
    <w:tbl> <!-- 表格开始 -->
      ...
    </w:tbl> <!-- 表格结束 -->
    <w:p>备注段落1</w:p>
    <w:p>备注段落2</w:p>
  </w:body>
</w:document>
``````





