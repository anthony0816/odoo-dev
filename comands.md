### init the server 
``` bash
python odoo-bin -c odoo.conf 
```

### create the base for building a module
```  bash
python odoo-bin scaffold custom_module modules
```

### create and .po for a determin language translation 
``` bash 
python .\odoo-bin -d database_name --addons-path=.\addons,.\your_folder --i18n-export=./the_route_till_language.po --modules=module_name --language=language
```
