# Pasta para arquivos estáticos (imagens, CSS, JS)

Coloque sua imagem `ifrn.jpg` nesta pasta.

Para usar a imagem nos templates, use:
```django
{% load static %}
<img src="{% static 'images/ifrn.jpg' %}" alt="IFRN">
```

## Estrutura:
- `static/images/` - Para imagens
- `static/css/` - Para arquivos CSS personalizados
- `static/js/` - Para arquivos JavaScript personalizados
