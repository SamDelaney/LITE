<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="html" version="4.0" encoding="UTF-8" omit-xml-declaration="yes" indent="yes"/>
	<xsl:template match="document">
		<!-- NOTE, this DOCTYPE causes issues for tests that use AssertThatXmlIn to catch an error and display the DOM -->
		<!-- <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html[]&gt;</xsl:text> -->

		<html>
			<head>
				<!-- ======================== -->
				<title>Interlinear text: "<xsl:value-of
						select="interlinear-text/item[@type='title']"/>"</title>
				<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
				<meta name="keywords" content="interlinear texts"/>
				<style>
					h1{
					    font:1.2em "Doulos SIL", "Charis SIL", "Times New Roman", Times, serif;
					    margin:0;
					    background-color:yellow;
					}
					.description{
					    display:inline;
					    font:normal 1em serif;
					}
					.textp{
					    border-bottom:solid black 1px;
					    font:bold 1.2em serif;
					}
					div.phrase{
					    display:inline-block;
					    margin-bottom:1em;
					    page-break-inside:avoid;
					    page-break-before:avoid;
					}
					.phrasenumber{
					    font:bold 1.2em serif;
					    display:inline;
					}
					p.phrasetables{
					    margin:-2.5em 0em 0em 2.5em;
					}
					.wordTable{
					    margin-top:1em;
					}
					td{
					    height:1em;
					    vertical-align:bottom;
					    white-space:nowrap;
					}
					span{
					    display:inline-block;
					    vertical-align:top;
					}
					.txt{
					    background-color:#BFE4FF;
					    font-size:1.2em;
					    font-family:"Doulos SIL", "Charis SIL", "Times New Roman", Times, serif;
					}
					.morph{
					    border:#BF8660 solid 1px;
					}
					.morphtxt{
					    background-color:#FFD9BF;
					    font-family:"Doulos SIL", "Charis SIL", "Times New Roman", Times, serif;
					}
					.morphcf{
					    background-color:#FFD880;
					    font-family:"Doulos SIL", "Charis SIL", "Times New Roman", Times, serif;
					}
					.morphgls{
					    background-color:#FFEC66;
					    font-style:italic;
					    font-family:Arial, sans-serif;
					}
					.morphmsa{
					    background-color:#FFD150;
					    font-family:Courier, monospace;
					}
					.gls{
					    background-color:#E6FFBF;
					    font:italic 1em Arial;
					}
					.pos{
					    background-color:#CCCC8F;
					    font-family:Courier, monospace;
					}
					.free{
					    display:inline;
					    background-color:#CCFFBF;
					    font:bold 1.1em serif;
					}
					
					.itx_Frame_Number{
					font:normal 1em serif;
					display:inline;
					}
					
					.lexMorphemeFrameNumber{
					font:normal 1em serif;
					display:inline;
					}
					
					.itxBaseline{
					    font-style:italic;
					}
					
					.lexMorpheme{
					    font-style:italic;
					}
					
					.lexGloss{
					    font-size:.9em;
					    color: maroon;
					}
					
					.itxFreeTranslation{
					    font:normal
					}
					
					.lit{
					    display:inline;
					    margin-left:1.9em;
					    background-color:#CCFFBF;
					    font:normal 1em serif;
					}
					.itxNotes{
					    margin-left:1em;
					    color:mediumblue;
					    font:normal 1em serif;
					}
					.ctrlfree{
					    display:inline;
					    margin-left:20px;
					    padding:5px;
					    background-color:#FFFFFF;
					}
					.punct{
					    margin-top:.1em;
					    padding:.8em .5em 0em .3em;
					    background-color:#80C9FF;
					    height:1.4em;
					    font:bold 1em serif;
					}
					.ctrl{
					    margin:0;
					    padding:2px 5px 3px 0px;
					}
					sub,
					sup{
					    display:none;
					}
					.hidden{
					    display:none;
					}</style>

				<script type="text/javascript"><xsl:text disable-output-escaping="yes">
<![CDATA[
function hasClass(ele,cls){
	return ele.className.match(new RegExp('(\\s|^)'+cls+'(\\s|$)'));
}
function addClass(ele,cls){
	if (!hasClass(ele,cls)) ele.className += " "+cls;
}
function removeClass(ele,cls){
	if (hasClass(ele,cls)){
		var reg = new RegExp('(\\s|^)'+cls+'(\\s|$)');
		ele.className=ele.className.replace(reg," ");
	}
}
function toggleClass(el,clsName){
	var x = document.getElementsByTagName(el);
	for(var i=0; i<x.length; i++){
		if(element("hide"+clsName).checked==false && hasClass(x[i],clsName)){
			addClass(x[i],"hidden");
		}
		if(element("hide"+clsName).checked==true && hasClass(x[i],clsName)){
			removeClass(x[i],"hidden");
		}
	}
}
// The function below is similar to above but is used to toggle the segment number span found on lexMorphemeFrameNumber
// in case the user hides the baseline. Note the toggle is reversed from above, and it is tied to the state of the hide baseline checkbox.
function toggleLexMorphemeFrameNumber(el,clsName){
	var x = document.getElementsByTagName(el);
	for(var i=0; i<x.length; i++){
		if(element("hideitxBaseline").checked==true && hasClass(x[i],clsName)){
			addClass(x[i],"hidden");
		}
		if(element("hideitxBaseline").checked==false && hasClass(x[i],clsName)){
			removeClass(x[i],"hidden");
		}
	}
}

function element(id){
	if(document.getElementById != null) {
		return document.getElementById(id);
	}
	if(document.all != null) {
		return document.all[id];
	}
	if(document.layers != null) {
		return document.layers[id];
	}
	return null;
}
]]></xsl:text>
					</script>

				<title> &#160; </title>
			</head>
			<body>
				<div id="control">
					<span class="ctrlabel">Display:</span>
					<!--This section outputs a checkbox for each type of interlinear line only if they exist-->
					<!--Checkbox for hiding itxBaseline row -->
					<span class="ctrl ctrlfree">
						<input checked="checked"
							onclick="toggleClass('tr','itxBaseline'); toggleLexMorphemeFrameNumber('span','lexMorphemeFrameNumber');"
							id="hideitxBaseline" value="itxBaseline" type="checkbox"/>
						<label for="hideitxBaseline">Baseline</label>
					</span>
					<!--Check to see if there are morphemic analyses present. If so, give user opportunity to hide those.-->
					<xsl:if test="//words/word/morphemes/morph">
						<!--Checkbox for hiding lexMorpheme row -->
						<span class="ctrl ctrlfree">
							<input checked="checked" onclick="toggleClass('tr','lexMorpheme');"
								id="hidelexMorpheme" value="lexMorpheme" type="checkbox"/>
							<label for="hidelexMorpheme">Morphemes</label>
						</span>
						<!--Checkbox for hiding lexGloss row -->
						<span class="ctrl ctrlfree">
							<input checked="checked" onclick="toggleClass('tr','lexGloss');"
								id="hidelexGloss" value="lexGloss" type="checkbox"/>
							<label for="hidelexGloss">Morpheme glosses</label>
						</span>
						<!--Checkbox for hiding lexPOS row -->
						<span class="ctrl ctrlfree">
							<input checked="checked" onclick="toggleClass('tr','lexPOS');"
								id="hidelexPOS" value="lexPOS" type="checkbox"/>
							<label for="hidelexPOS">Morpheme parts-of-speech</label>
						</span>
					</xsl:if>

					<!--Checkbox for hiding free translation row-->
					<xsl:if test="//phrase/item[@type='gls']">
						<span class="ctrl ctrlfree">
							<input checked="checked"
								onclick="toggleClass('tr','itxFreeTranslation');"
								id="hideitxFreeTranslation" value="itxFreeTranslation"
								type="checkbox"/>
							<label for="hideitxFreeTranslation">free translation</label>
						</span>
					</xsl:if>

					<!--Checkbox for hiding literal translation row-->
					<xsl:if test="//phrase/item[@type='lit']">
						<span class="ctrl ctrlfree">
							<input checked="checked"
								onclick="toggleClass('tr','itxLiteralTranslation');"
								id="hideitxLiteralTranslation" value="itxLiteralTranslation"
								type="checkbox"/>
							<label for="hideitxLiteralTranslation">literal translation</label>
						</span>
					</xsl:if>

					<!--Checkbox for hiding notes row(s)-->
					<xsl:if test="//phrase/item[@type='note']">
						<span class="ctrl ctrlfree">
							<input checked="checked" onclick="toggleClass('p','itxNotes');"
								id="hideitxNotes" value="itxNotes" type="checkbox"/>
							<label for="hideitxNotes">notes</label>
						</span>
					</xsl:if>

					<!--
						&#160;&#160;<small>Best viewed with <a href="http://www.mozilla.com"
								><img border="0" alt="Firefox 3" title="Firefox 3"
								src="http://sfx-images.mozilla.org/affiliates/Buttons/firefox3/FF3_80x15_o.png"
							/></a></small>
					-->

				</div>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<!-- INTERLINEAR-TEXT LEVEL -->

	<xsl:template match="interlinear-text">
		<xsl:apply-templates/>
	</xsl:template>

	<!--<xsl:template match="interlinear-text/item">
		<xsl:apply-templates/>
	</xsl:template>-->

	<xsl:template match="interlinear-text/item[@type='title']">
		<h1>
			<xsl:attribute name="lang"> Title: <xsl:value-of select="@lang"/>
			</xsl:attribute>
			<xsl:apply-templates/>
		</h1>
	</xsl:template>
	<xsl:template match="interlinear-text/item[@type='title-abbreviation']"/>
	<xsl:template match="interlinear-text/item[@type='source']">
		<h2>
			<xsl:apply-templates/>
		</h2>
	</xsl:template>
	<xsl:template match="interlinear-text/item[@type='description']">
		<h2>
			<xsl:apply-templates/>
		</h2>
	</xsl:template>

	<!-- PARAGRAPH LEVEL -->

	<xsl:template match="paragraphs">
		<xsl:apply-templates/>
	</xsl:template>

	<xsl:template match="paragraph">
		<xsl:apply-templates/>
	</xsl:template>

	<!-- PHRASE LEVEL -->

	<xsl:template match="phrases">
		<xsl:apply-templates/>
	</xsl:template>
	<!--A flextext phrase is a FLEx segment-->
	<xsl:template match="phrase">
		<!--The segment number is stored in a variable. The variable is placed in the first column of the baseline and also in a hidden span of the morpheme line
			in case the baseline is hidden by the user-->
		<xsl:variable name="vSegmentNumber" select="item[@type='segnum']"/>
		<table class="itx_Words">
			<tbody>
				<!--Segment number and baseline words-->
				<tr class="itxBaseline">
					<!--Segment number-->
					<td>
						<span class="itx_Frame_Number">
							(<xsl:value-of select="$vSegmentNumber"/>)
						</span>
					</td>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word/item[@type='txt' or @type='punct'] ">
						<td class="itxBaseline">
							<xsl:value-of select="text()"/>
						</td>
					</xsl:for-each>
				</tr>
				<!-- Lexemes row-->
				<!-- Note that the affix dashes are included in the morph, whereas in the gloss and the POS they are not-->
				<tr class="lexMorpheme">
					<!--Space in cell in column where the example number is housed-->
					<td>
						<span class="lexMorphemeFrameNumber hidden">
							(<xsl:value-of select="$vSegmentNumber"/>)
						</span>
					</td>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<!--Want to include punctuation in the morpheme line in case the user decides to hide the baseline, which is standard Leipzig practice-->
						<xsl:choose>
							<xsl:when test="item[@type='punct']">
								<td>
									<xsl:value-of select="item/text()"/>
								</td>
							</xsl:when>
							<xsl:otherwise>
								<td>
									<xsl:for-each select="morphemes/morph">
										<xsl:value-of select="item[@type='cf']/text()"/>
									</xsl:for-each>
								</td>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:for-each>
				</tr>
				<!-- LexGloss row-->
				<tr class="lexGloss">
					<!--Space in cell in column where the example number is housed-->
					<td>&#32;</td>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<td>
							<xsl:for-each select="morphemes/morph">
								<xsl:if test="@type='suffix' or @type='suffixing interfix' or @type='infix'">
									<xsl:text>-</xsl:text>
								</xsl:if>
								<xsl:if test="@type='enclitic'">
									<xsl:text>=</xsl:text>
								</xsl:if>
								<!--Need to test for FUNCTOR GLOSSES as substrings here and style as SMALL CAPS.
					Might be best to compare against a master list of functor morphemes glosses. -->
								<xsl:variable name="startcase"
									>ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
								<xsl:variable name="endcase"
									>ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘQʀꜱᴛᴜᴠᴡxʏᴢ</xsl:variable>
								<!--<xsl:value-of select="item[@type='gls']/text()"/>-->
								<xsl:value-of
									select="translate(item[@type='gls']/text(), $startcase, $endcase)"/>
								<!--<font style="font-variant: small-caps"><xsl:value-of select="translate(., $startcase, $endcase)"/></font>-->
								<xsl:if test="@type='prefix' or @type='prefixing interfix' or @type='infix'">
									<xsl:text>-</xsl:text>
								</xsl:if>
								<xsl:if test="@type='proclitic'">
									<xsl:text>=</xsl:text>
								</xsl:if>
							</xsl:for-each>
						</td>
					</xsl:for-each>
				</tr>
				<!-- LexPOS row-->
				<!--Temporarily getting rid of this *********-->
				<!--tr class="morphmsa">
					<td/>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<td class="LexPOS">
							<xsl:for-each select="morphemes/morph">
								<xsl:if test="@type='suffix'">
									<xsl:text>-</xsl:text>
								</xsl:if>
								<xsl:value-of select="item[@type='msa']/text()"/>
								<xsl:if test="@type='prefix'">
									<xsl:text>-</xsl:text>
								</xsl:if>
							</xsl:for-each>
						</td>
					</xsl:for-each>
				</tr-->

				<!-- Word Gloss rows still need to be done-->

				<!--In order to get the colspan correct, we need to count number of columns from above-->
				<xsl:variable name="vNumWords">
					<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"/>
				</xsl:variable>
				<!-- If Free translations exist for the segment then create Free translation row-->
				<xsl:if test="item[@type='gls']">
					<tr class="itxFreeTranslation">
						<td/>
						<td>
							<xsl:attribute name="colspan">
								<xsl:value-of select="$vNumWords"/>
							</xsl:attribute> &apos;<xsl:value-of select="item[@type='gls']"/>&apos;
						</td>
					</tr>
				</xsl:if>
				<!-- If Literal translations exist for the segment then create Lit translation row-->
				<xsl:if test="item[@type='lit']">
					<tr class="itxLiteralTranslation">
						<td/>
						<td>
							<xsl:attribute name="colspan">
								<xsl:value-of select="$vNumWords"/>
							</xsl:attribute> Lit: &apos;<xsl:value-of select="item[@type='lit']"
							/>&apos; </td>
					</tr>
				</xsl:if>
			</tbody>
		</table>
		<!-- Notes are little funky if they are contained in the same table as the interlinear due to their possible length compared to that of the segment. 
					To compensate for this, we create a paragraph for each note. -->
		<xsl:if test="item[@type='note']">
			<xsl:for-each select="item[@type='note']">
				<p class="itxNotes">
				Note: <xsl:value-of select="."/>
				</p>
			</xsl:for-each>
		</xsl:if>
		<hr/>
	</xsl:template>
	<!--Items on flextext phrases included the segment number, the free translation, the literal translation and any notes
	Below we start with the segment number which, for paper-writing purposes will be changed to a sequential example number.-->

	<!--??Not sure - baseline text only in unanalyzed form perhaps?-->
	<xsl:template name="tBaseLine" match="phrase/item[@type='txt']">
		<xsl:apply-templates/>
		<br/>
	</xsl:template>

	<!-- 2nd Row - Morphemes -->
	<xsl:template match="words">
		<tr>
			<td class="itx_lexemes">
				<xsl:for-each select="morph/item[@type='cf']">
					<xsl:value-of select="."/>
				</xsl:for-each>
			</td>
		</tr>
	</xsl:template>
	<!--3rd Row - Lexemes -->

	<!--4th Row - LexGlossesEng -->

	<!--5th Row - LexPOS -->
	<!--Free translation on the segment-->
	<xsl:template match="phrase/item[@type='gls']">
		<xsl:variable name="vNumWords">
			<xsl:value-of select="count(../words/word[item[@type='txt']])"/>
		</xsl:variable>
		<tr class="itx_Freeform_gls">
			<td/>
			<td>
				<xsl:attribute name="colspan">
					<xsl:value-of select="$vNumWords"/>
				</xsl:attribute>
				<xsl:apply-templates/>
			</td>
		</tr>
	</xsl:template>
	<!--Literal translation on the segment-->
	<xsl:template match="phrase/item[@type='lit']">
		<xsl:variable name="vNumWords">
			<xsl:value-of select="count(../words/word[item[@type='txt']])"/>
		</xsl:variable>
		<tr class="itxLiteralTranslation">
			<td/>
			<td>
				<xsl:attribute name="colspan">
					<xsl:value-of select="$vNumWords"/>
				</xsl:attribute>
				<xsl:apply-templates/>
			</td>
		</tr>
	</xsl:template>
	<!--Notes on the segment. Because this is applied against any phrase\item, multiple notes are handled here without problem.-->
	<xsl:template match="phrase/item[@type='note']">
		<xsl:variable name="vNumWords">
			<xsl:value-of select="count(../words/word[item[@type='txt']])"/>
		</xsl:variable>
		<tr class="itxNotes">
			<td/>
			<td>
				<xsl:attribute name="colspan">
					<xsl:value-of select="$vNumWords"/>
				</xsl:attribute>
				<xsl:apply-templates/>
			</td>
		</tr>
	</xsl:template>

	<!-- WORD LEVEL -->
	<!-- In terms of the hierarchy, we are here: paragraphs\paragraph\phrases\words
	A FLEx segment contains words which in turn are analyzed.-->
	<xsl:template match="words">
		<xsl:variable name="vNumWords">
			<xsl:value-of select="count(word/item[@type='txt'])"/>
		</xsl:variable>
		<xsl:for-each select="word/item[@type='txt']">
			<td class="itxBaseline">
				<xsl:apply-templates/>
				<xsl:text>&#160;</xsl:text>
			</td>
		</xsl:for-each>
	</xsl:template>

	<!-- MISCELLANEOUS -->

	<xsl:template match="i">
		<i>
			<xsl:apply-templates/>
		</i>
	</xsl:template>

	<xsl:template match="b">
		<b>
			<xsl:apply-templates/>
		</b>
	</xsl:template>

	<xsl:template match="title">
		<block font-style="bold">
			<xsl:apply-templates/>
		</block>
	</xsl:template>


	<xsl:template match="*">
		<xsl:copy>
			<xsl:copy-of select="@*"/>
			<xsl:apply-templates/>
		</xsl:copy>
	</xsl:template>

</xsl:stylesheet>
