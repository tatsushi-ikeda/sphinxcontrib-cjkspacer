
Welcome to Test for sphinxcontrib.cjkspacer
============================================================

1. without space
2. with `sphinxcontrib.trimblank` and `sphinxcontrib.cjkspacer`
3. with half-width space

MAIN
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
