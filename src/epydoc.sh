#!/bin/sh

#configurar los paths
DESDE=/home/fran/flaskadd/proyectois2/sicpX/src

cd $DESDE
epydoc $DESDE/manage.py
mv $DESDE/html $DESDE/docsManage/
epydoc $DESDE/sicp.py
mv $DESDE/html $DESDE/docsSicp/
epydoc $DESDE/form.py
mv $DESDE/html $DESDE/docsForm/
epydoc $DESDE/models.py
mv $DESDE/html $DESDE/docsModel/
