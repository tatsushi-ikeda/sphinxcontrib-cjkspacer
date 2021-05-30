============================================================
Japanese Demo (日本語デモ) for `sphinxcontrib.cjkspacer`
============================================================

.. meta::
   :description: A Sphinx extension, which inserts spacer elements between the Chinese Japanese Korean (CJK) characters and the other characters. 日本語を含むCJK文字とその他の文字種の間での空き量(スペース)調整機能を与えるSphinx拡張です。
   :keywords: Python, Sphinx, CJK Languages, Japanese, Space, 日本語, スペース

Homepage: https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer


.. raw:: html

   <input id="toggle" type='checkbox'/>
   <span>Highlight the inserted spacers (挿入されたspacer<span class="cjkspacer"></span>を強調表示)</span>
         
From `README.md <https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/blob/master/README.md>`_
===================================================================================================

With `sphinxcontrib.trimblank` and `sphinxcontrib.cjkspacer`
------------------------------------------------------------

    A `Sphinx <https://www.sphinx-doc.org/en/master/>`_ extension, which inserts spacer elements between the Chinese Japanese Korean (CJK) characters and the other characters.

    Some of the word processors, e.g., Microsoft® Word and TeX (at least in the case of pTeX), adjust the distances (spaces) between the CJK characters and the others automatically (c.f. `Requirements for Japanese Text Layout#spacing between characters <https://www.w3.org/TR/jlreq/#spacing_between_characters>`_).
    Unfortunately, however, HTML with CSS does not have this function as of CSS3 (See the `text-spacing` property discussed in some old versions of W3C® Working Draft, e.g., `1 September 2011 <https://www.w3.org/TR/2011/WD-css3-text-20110901/>`_ and `19 January 2012 <https://www.w3.org/TR/2012/WD-css3-text-20120119/>`_).
    This Sphinx extension provides an alternative function to adjust such distances.


    異なる種類の文字種間の空き量(スペース)を調整する機能を持たないフォーマットに、日本語を含むCJK文字とその他の文字種の間での空き量調整機能を与えるSphinx拡張です。
    この拡張と `sphinxcontrib-trimblank <https://github.com/amedama41/sphinxcontrib-trimblank>`_ などを併用することで、HTML出力において、数字／英語と日本語の間への手動での半角スペース挿入・除去を行うよりも自然な仕上がりを実現することを目指しています(`日本語によるデモ <https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/>`_)。
    
    ただし、現状では `組版処理の要件(日本語版) <https://www.w3.org/TR/2009/NOTE-jlreq-20090604/ja/>`_ に記載されているような高度な調整は行っておらず、2種の判断基準による1種類の空き量しか導入していません。
    CSS3で延期された `text-spacing` が今後CSS4などで導入されればこの拡張は不要になることでしょう。

Without the extensions
------------------------------------------------------------

.. raw:: html
   
    <blockquote>
    <div><p>異なる種類の文字種間の空き量(スペース)を調整する機能を持たないフォーマットに、日本語を含むCJK文字とその他の文字種の間での空き量調整機能を与えるSphinx拡張です。この拡張と<a class="reference external" href="https://github.com/amedama41/sphinxcontrib-trimblank">sphinxcontrib-trimblank</a>などを併用することで、HTML出力において、数字／英語と日本語の間への手動での半角スペース挿入・除去を行うよりも自然な仕上がりを実現することを目指しています(<a class="reference external" href="https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/">日本語によるデモ</a>)。</p>
    <p>ただし、現状では<a class="reference external" href="https://www.w3.org/TR/2009/NOTE-jlreq-20090604/ja/">組版処理の要件(日本語版)</a>に記載されているような高度な調整は行っておらず、2種の判断基準による1種類の空き量しか導入していません。CSS3で延期された<cite>text-spacing</cite>が今後CSS4などで導入されればこの拡張は不要になることでしょう。</p>
    </div>
    </blockquote>

Demo
============================================================

1. スペースなし
    (without spaces)
   
2. `sphinxcontrib.trimblank` ・ `sphinxcontrib.cjkspacer` 拡張による調整
    (with `sphinxcontrib.trimblank` and `sphinxcontrib.cjkspacer`)

3. 半角スペースあり
    (with half-width spaces)

TEXT
------------------------------------------------------------
.. code-block:: ReST

   あいうえおabcdいろはにほへと01234数字:あAいB,
                
.. |main-without-space| raw:: html

   <span>あいうえおabcdいろはにほへと01234数字:あAいB</span>

.. |main-with-space| raw:: html

   <span>あいうえお abcd いろはにほへと 01234 数字: あ A い B</span>

.. raw:: html
   
   <div class='cjkspacer-sample'>

1. |main-without-space|
  
2. あいうえおabcdいろはにほへと01234数字:あAいB
  
3. |main-with-space|

.. raw:: html
   
   </div>

EM
------------------------------------------------------------

.. code-block:: ReST

   あいうえお *abcd* いろ *はに* ほへと *01234数* 字 *:あAいB*

.. |em-without-space| raw:: html

   <span>あいうえお<em>abcd</em>いろ<em>はに</em>ほへと<em>01234数</em>字<em>:あAいB</em></span>

.. |em-with-space| raw:: html

   <span>あいうえお <em>abcd</em> いろ<em>はに</em>ほへと <em>01234 数</em>字<em>: あ A い B</em></span>
                                
.. raw:: html
   
   <div class='cjkspacer-sample'>

1. |em-without-space|
  
2. あいうえお *abcd* いろ *はに* ほへと *01234数* 字 *:あAいB*
  
3. |em-with-space|

.. raw:: html
   
   </div>

STRONG
------------------------------------------------------------
.. code-block:: ReST

   あいうえお **abcd** いろ **はに** ほへと **01234数** 字 **:あAいB**
  
.. |strong-without-space| raw:: html

   <span>あいうえお<strong>abcd</strong>いろ<strong>はに</strong>ほへと<strong>01234数</strong>字<strong>:あAいB</strong></span>

.. |strong-with-space| raw:: html

   <span>あいうえお <strong>abcd</strong> いろ<strong>はに</strong>ほへと <strong>01234 数</strong>字<strong>: あ A い B</strong></span>
                                
.. raw:: html
   
   <div class='cjkspacer-sample'>

1. |strong-without-space|
  
2. あいうえお **abcd** いろ **はに** ほへと **01234数** 字 **:あAいB**
  
3. |strong-with-space|

.. raw:: html
   
   </div>

CODE
------------------------------------------------------------
.. code-block:: ReST

   あいうえお ``abcd`` いろ ``はに`` ほへと ``01234数`` 字 ``:あAいB``

.. |code-without-space| raw:: html

   <span>あいうえお<code class="docutils literal notranslate"><span class="pre">abcd</span></code>いろ<code class="docutils literal notranslate"><span class="pre">はに</span></code>ほへと<code class="docutils literal notranslate"><span class="pre">01234数</span></code>字<code class="docutils literal notranslate"><span class="pre">:あAいB</span></code></span>

.. |code-with-space| raw:: html

   <span>あいうえお <code class="docutils literal notranslate"><span class="pre">abcd</span></code> いろ<code class="docutils literal notranslate"><span class="pre">はに</span></code>ほへと <code class="docutils literal notranslate"><span class="pre">01234 数</span></code>字<code class="docutils literal notranslate"><span class="pre"> : あ A い B</span></code></span>

.. raw:: html
   
   <div class='cjkspacer-sample'>

1. |code-without-space|
  
2. あいうえお ``abcd`` いろ ``はに`` ほへと ``01234数`` 字 ``:あAいB``
  
3. |code-with-space|

.. raw:: html
   
   </div>

PARENTHESES & PUNCTUATION
------------------------------------------------------------
.. code-block:: ReST

   括弧(Parenthesies):Parenthesis(括弧),コンマ,ピリオド.読点、句点。 スペース Space.

.. |pp-without-space| raw:: html

   括弧(Parentheses):Parentheses(括弧),コンマ,ピリオド.読点、句点。  スペース  Space.

.. |pp-with-space| raw:: html

   括弧 (Parentheses) : Parentheses (括弧) , コンマ , ピリオド. 読点、句点。スペース Space.

.. raw:: html
   
   <div class='cjkspacer-sample'>

1. |pp-without-space|
2. 括弧(Parentheses):Parentheses(括弧),コンマ,ピリオド.読点、句点。  スペース  Space.
3. |pp-with-space|

.. raw:: html
   
   </div>

CJK SYMBOLS & PUNCTUATION
------------------------------------------------------------
.. code-block:: ReST

   A　あ　1 A、あ、1 A。あ。1 A〈あ〈1 A〉あ〉1 A《あ《1 A》あ》1 A「あ「1 A」あ」1 A『あ『1 A』あ』1 A【あ【1 A】あ】1 A〔あ〔1 A〕あ〕1 A〖あ〖1 A〗あ〗1 A〘あ〘1 A〙あ〙1 A〚あ〚1 A〛あ〛1 A・あ・1 A！あ！1 A＂あ＂1 A＇あ＇1 A（あ（1 A）あ）1 A，あ，1 A．あ．1 A／あ／1 A：あ：1 A；あ；1 A？あ？1 A［あ［1 A＼あ＼1 A］あ］1 A｛あ｛1 A｜あ｜1 A｝あ｝1 A｟あ｟1 A｠あ｠1
                
.. raw:: html
   
   <div class='cjkspacer-sample'>

A　あ　1 A、あ、1 A。あ。1 A〈あ〈1 A〉あ〉1 A《あ《1 A》あ》1 A「あ「1 A」あ」1 A『あ『1 A』あ』1 A【あ【1 A】あ】1 A〔あ〔1 A〕あ〕1 A〖あ〖1 A〗あ〗1 A〘あ〘1 A〙あ〙1 A〚あ〚1 A〛あ〛1 A・あ・1 A！あ！1 A＂あ＂1 A＇あ＇1 A（あ（1 A）あ）1 A，あ，1 A．あ．1 A／あ／1 A：あ：1 A；あ；1 A？あ？1 A［あ［1 A＼あ＼1 A］あ］1 A｛あ｛1 A｜あ｜1 A｝あ｝1 A｟あ｟1 A｠あ｠1

.. raw:: html
   
   </div>

Note that Ideographicl Space (　) is trimmed by `sphinxcontrib.trimblank`.

.. raw:: html
   
     <script>
      $(":checkbox").on('click', function(){
         $(".cjkspacer").toggleClass("cjkspacer-highlight")
      });
    </script>

