<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
	<xsl:output method="text" encoding="UTF-8" omit-xml-declaration="yes" indent="no"/>
	<xsl:strip-space elements="*"/>
	<xsl:template match="document">
		<!--<xsl:result-document href="{concat(interlinear-text/item[@type='title'][@lang='en'],'.txt')}" method="text" encoding="UTF-8">
			<xsl:apply-templates/>
		</xsl:result-document>-->
		<xsl:apply-templates/>
	</xsl:template>
	<!--<xsl:template match="/">
		<xsl:for-each select="document">
			<xsl:apply-templates/>
		</xsl:for-each>
	</xsl:template>-->
	<!-- INTERLINEAR-TEXT LEVEL -->
	<xsl:template match="interlinear-text">
		<!--<xsl:result-document href="{concat(substring(item[@type='title'][@lang='en'],1,5),'.txt')}" method="text" encoding="UTF-8" indent="no">
			<xsl:apply-templates/>
		</xsl:result-document>-->
		<xsl:variable name="vTextNumber" select="position()"/>
		<xsl:choose>
			<xsl:when test="item[1][@type='title']">
				<xsl:variable name="vPossibleIllegalNameChars"
					>!,;:.()[]=-?$#</xsl:variable>
				<!--<xsl:variable name="vTextName" select="item[1][@type='title']"/>-->
				<xsl:variable name="vTextName">
					<xsl:if test="item[1][@type='title-abbreviation']"></xsl:if>
					<xsl:choose>
						<xsl:when test="item[1][@type='title-abbreviation']">
							<xsl:value-of select="item[1][@type='title-abbreviation']"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="item[1][@type='title']"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:variable>
				<!--Here we remove illegal characters from filename-->
				<xsl:variable name="vTextFileName" select="translate($vTextName, $vPossibleIllegalNameChars,'_')"/>			
				<xsl:result-document href="{concat($vTextFileName,'_',$vTextNumber,'.txt')}" method="text" encoding="UTF-8" indent="no">
					<xsl:apply-templates/>
				</xsl:result-document>
			</xsl:when>
			<xsl:otherwise>
				<xsl:result-document href="{concat('untitled_',$vTextNumber,'.txt')}" method="text" encoding="UTF-8" indent="no">
					<xsl:apply-templates/>
				</xsl:result-document>
			</xsl:otherwise>
		</xsl:choose>
<!--		<xsl:result-document href="{concat(item[1][@type='title']/node(),'.txt')}" method="text" encoding="UTF-8" indent="no">
			<xsl:apply-templates/>
		</xsl:result-document>-->
	</xsl:template>
	<!--Do nothing with the title, etc. for now-->
	<xsl:template match="interlinear-text/item"/>

	<!--<xsl:template match="interlinear-text/item[@type='title']">
		<h1>
			<xsl:attribute name="lang"> Title: <xsl:value-of select="@lang"/>
			</xsl:attribute>
			<xsl:apply-templates/>
		</h1>
	</xsl:template>-->
	<!--<xsl:template match="interlinear-text/item[@type='title-abbreviation']"/>
	<xsl:template match="interlinear-text/item[@type='source']">
		<h2>
			<xsl:apply-templates/>
		</h2>
	</xsl:template>-->
	<!--<xsl:template match="interlinear-text/item[@type='description']">
		<h2>
			<xsl:apply-templates/>
		</h2>
	</xsl:template>-->
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
		<!--<xsl:value-of select="normalize-space(.)"/>-->

		<!--The segment number is stored in a variable. The variable is placed in the first column of the baseline and also in a hidden span of the morpheme line
			in case the baseline is hidden by the user-->
		<xsl:variable name="vSegmentNumber" select="item[@type='segnum']/node()"/>
		<xsl:variable name="vNumWords">
			<xsl:value-of select="count(words/word/item[@type='txt' or @type='punct'])"/>
		</xsl:variable>
		<!--Segment number-->
		<xsl:value-of select="$vSegmentNumber"/>
		<xsl:text>. </xsl:text>
		<!--Here we go through each word and put spaces if followed by another word-->
		<xsl:for-each select="words/word[item[@type='txt' or @type='punct']]">
			<xsl:value-of select="item/text()"/>
			<!--If the next word has an item of @type = txt then put a space after it. -->
			<xsl:if test="contains(following-sibling::word[1]/item[1]/@type, 'txt')">
				<xsl:text>&#32;</xsl:text>
			</xsl:if>
		</xsl:for-each>
		<xsl:text>&#13;&#10;</xsl:text>
	</xsl:template>
	<!--<xsl:template match="*">
		<xsl:copy>
			<xsl:copy-of select="@*"/>
			<xsl:apply-templates/>
		</xsl:copy>
	</xsl:template>-->
</xsl:stylesheet>
