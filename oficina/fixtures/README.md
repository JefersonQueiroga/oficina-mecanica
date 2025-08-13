# Comando para carregar dados iniciais

Para carregar os dados de exemplo no banco, execute:

```bash
python manage.py loaddata dados_iniciais
```

## Dados que serão criados:

### Veículos (5):
- ABC1234 - Volkswagen Gol 1.0
- DEF5678 - Fiat Uno Mille  
- GHI9012 - Honda Civic 2.0
- JKL3456 - Toyota Corolla 1.8
- MNO7890 - Chevrolet Onix 1.4

### Motoristas (5):
- João Silva Santos
- Maria Oliveira Costa
- Pedro Almeida Ferreira
- Ana Carolina Souza
- Carlos Eduardo Lima

### Oficinas (5):
- Auto Mecânica Silva
- Oficina do João
- Mecânica Rápida Ltda
- Centro Automotivo Norte
- Oficina Especializada RN

### Serviços de Manutenção (5):
- Diversos serviços vinculando veículos, motoristas e oficinas

## Para limpar os dados:
```bash
python manage.py flush
```

## Para recriar apenas as tabelas:
```bash
python manage.py migrate --run-syncdb
```
