#!/bin/bash

ARQ_RESULTADO_ZIP="D_lotfac.zip"
URL_RESULTADO="http://www1.caixa.gov.br/loterias/_arquivos/loterias/$ARQ_RESULTADO_ZIP"

	wget $URL_RESULTADO

	unzip -o $ARQ_RESULTADO_ZIP
	rm LOTFACIL.GIF D_lotfac.zip

