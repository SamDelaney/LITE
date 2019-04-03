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
				<style type="text/css" media="print" rel="stylesheet">
					#control{
					    display:none;
					}
					h1{
					    font:1.5em "Doulos SIL", "Charis SIL", "Times New Roman", Times, serif;
					    margin:0;
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
					    display:-moz-inline-box;
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
					    display:-moz-inline-box;
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
					.lit{
					    display:inline;
					    margin-left:1.9em;
					    background-color:#CCFFBF;
					    font:normal 1em serif;
					}
					.note{
					    display:inline;
					    margin-left:1.9em;
					    background-color:#CCFFBF;
					    font:normal 1em serif;
					}
					.ctrlfree{
					    display:inline;
					    margin-left:20px;
					    padding:5px;
					    background-color:#CCFFBF;
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
					}
				</style>

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
					<span class="ctrlabel">Display Interlinear Lines: </span>
					<!--This section outputs a checkbox for each type of interlinear line only if they exist-->
					<xsl:if test="//morphemes">
						<span class="ctrl morph"><input checked="checked"
								onclick="toggleClass('tr','morphemegroup');" id="hidemorphemegroup"
								value="morphemegroup" type="checkbox"/><label
								for="hidemorphemegroup">Morpheme Group</label></span>
					</xsl:if>
					<xsl:if test="//item[@type='txt']">
						<span class="ctrl morphtxt"><input checked="checked"
								onclick="toggleClass('tr','morphtxt');" id="hidemorphtxt"
								value="morphtxt" type="checkbox"/><label for="hidemorphtxt">MG
								morpheme</label></span>
					</xsl:if>
					<xsl:if test="//item[@type='cf']">
						<span class="ctrl morphcf"><input checked="checked"
								onclick="toggleClass('tr','morphcf');" id="hidemorphcf"
								value="morphcf" type="checkbox"/><label for="hidemorphcf">MG
								ref.</label></span>
					</xsl:if>
					<xsl:if test="//phrase/words/word/morphemes/morph/item[@type='gls']">
						<span class="ctrl morphgls"><input checked="checked"
								onclick="toggleClass('tr','morphgls');" id="hidemorphgls"
								value="morphgls" type="checkbox"/><label for="hidemorphgls">MG
								gloss</label></span>
					</xsl:if>
					<xsl:if test="//item[@type='msa']">
						<span class="ctrl morphmsa"><input checked="checked"
								onclick="toggleClass('tr','morphmsa');" id="hidemorphmsa"
								value="morphmsa" type="checkbox"/><label for="hidemorphmsa">MG gram.
								info</label></span>
					</xsl:if>
					<xsl:if test="//item[@type='gls']">
						<span class="ctrl gls"><input checked="checked"
								onclick="toggleClass('tr','gls');" id="hidegls" value="gls"
								type="checkbox"/><label for="hidegls">word gloss</label></span>
					</xsl:if>
					<!--		<xsl:if test="//morph[@type='stem']">
			<span class="ctrl morpheme"><input checked="checked" onclick="toggleClass('table','morph');" id="hidemorph" value="morph" type="checkbox" /><label for="hidemorph">morpheme</label></span>
		</xsl:if>-->
					<xsl:if test="//item[@type='pos']">
						<span class="ctrl pos"><input checked="checked"
								onclick="toggleClass('tr','pos');" id="hidepos" value="pos"
								type="checkbox"/><label for="hidepos">pos</label></span>
					</xsl:if>
					<xsl:if test="//phrase/item[@type='gls']">
						<span class="ctrl ctrlfree"><input checked="checked"
								onclick="toggleClass('span','free');" id="hidefree" value="free"
								type="checkbox"/><label for="hidefree">free
							translation</label></span>
					</xsl:if> &#160;&#160;<small>Best viewed with <a href="http://www.mozilla.com"
								><img border="0" alt="Firefox 3" title="Firefox 3"
								src="http://sfx-images.mozilla.org/affiliates/Buttons/firefox3/FF3_80x15_o.png"
							/></a></small>
				</div>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<!-- INTERLINEAR-TEXT LEVEL -->

	<xsl:template match="interlinear-text">
		<xsl:apply-templates/>
	</xsl:template>

	<xsl:template match="interlinear-text/item">
		<xsl:apply-templates/>
	</xsl:template>

	<xsl:template match="interlinear-text/item[@type='title']">
		<h1>
			<xsl:attribute name="lang">
				<xsl:value-of select="@lang"/>
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
	<!--A flextext phrase is a FLEx segment
	In most cases, we probably do not need the FLEx segment number. At least for LITE 1.0-->
	<xsl:template match="phrase">
		<table class="itx_Words">
			<tbody>
				<!--Segment number and baseline words-->
				<tr class="itx_txt">
					<!--Segment number-->
					<td>
						<span class="itx_Frame_Number">
							<xsl:value-of select="item[@type='segnum']"/>
						</span>
					</td>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word/item[@type='txt' or @type='punct'] ">
						<td class="itx_txt">
							<xsl:value-of select="text()"/>
						</td>
					</xsl:for-each>
				</tr>
				<!-- Morphemes row-->
				<tr>
					<td/>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<td class="itx_morph">
							<xsl:for-each select="morphemes/morph">
								<xsl:value-of select="item[@type='txt']/text()"/>
							</xsl:for-each>
						</td>
					</xsl:for-each>
				</tr>
				<!-- Lexemes row-->
				<tr>
					<td/>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<td class="itx_morph">
							<xsl:for-each select="morphemes/morph">
								<xsl:value-of select="item[@type='cf']/text()"/>
							</xsl:for-each>
						</td>
					</xsl:for-each>
				</tr>
				<!-- LexGloss row-->
				<tr>
					<td/>
					<xsl:variable name="vNumWords">
						<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"
						/>
					</xsl:variable>
					<xsl:for-each select="words/word">
						<td class="lexGloss">
							<xsl:for-each select="morphemes/morph">
								<xsl:if test="@type='suffix'">
									<xsl:text>-</xsl:text>
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
								<xsl:if test="@type='prefix'">
									<xsl:text>-</xsl:text>
								</xsl:if>
							</xsl:for-each>
						</td>
					</xsl:for-each>
				</tr>
				<!-- LexPOS row-->
				<tr class="morphmsa">
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
				</tr>
				<!-- Word Gloss rows still need to be done-->

				<!--In order to get the colspan correct, we need to count number of columns from above-->
				<xsl:variable name="vNumWords">
					<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"/>
				</xsl:variable>
				<!-- Free translation row-->
				<tr class="itx_Freeform_gls">
					<td/>
					<td>
						<xsl:attribute name="colspan">
							<xsl:value-of select="$vNumWords"/>
						</xsl:attribute>
						<xsl:value-of select="item[@type='gls']"/>
					</td>
				</tr>
				<!-- Lit translation row-->
				<tr class="itx_Freeform_lit">
					<td/>
					<td>
						<xsl:attribute name="colspan">
							<xsl:value-of select="$vNumWords"/>
						</xsl:attribute>
						<xsl:value-of select="item[@type='lit']"/>
					</td>
				</tr>
				<!-- Lit translation row-->
				<tr class="itx_Freeform_note">
					<td/>
					<td>
						<xsl:attribute name="colspan">
							<xsl:value-of select="$vNumWords"/>
						</xsl:attribute>
						<xsl:value-of select="item[@type='note']"/>
					</td>
				</tr>
			</tbody>
		</table>
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
		<tr class="itx_Freeform_lit">
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
		<tr class="itx_Freeform_note">
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
			<td class="itx_txt">
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
