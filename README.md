# Sistema de Oficina Mecânica - IFRN

Sistema de controle de manutenção desenvolvido em Django para gerenciar veículos, motoristas, oficinas e serviços de manutenção.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Git (opcional, para clonar o repositório)
- Windows 10/11

## 🚀 Instalação e Configuração

### 1. Clone o repositório (ou baixe o ZIP)

```powershell
git clone https://github.com/JefersonQueiroga/oficina-mecanica.git
cd oficina-mecanica
```

### 2. Crie um ambiente virtual

```powershell
python -m venv venv
```

### 3. Ative o ambiente virtual

```powershell
.\venv\Scripts\activate
```

### 4. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 5. Execute as migrações do banco de dados

```powershell
python manage.py migrate
```

### 6. Carregue os dados de exemplo

```powershell
python manage.py loaddata dados_iniciais
```

### 7. Crie um superusuário (opcional)

```powershell
python manage.py createsuperuser
```

### 8. Inicie o servidor de desenvolvimento

```powershell
python manage.py runserver
```

## 🌐 Acessando a aplicação

- **Site principal:** http://127.0.0.1:8000/
- **Painel administrativo:** http://127.0.0.1:8000/admin/

## 📂 Estrutura do Projeto

```
oficina-mecanica/
├── core/                   # Configurações do Django
├── oficina/               # App principal
│   ├── models.py         # Modelos de dados
│   ├── views.py          # Views (function-based)
│   ├── forms.py          # Formulários
│   ├── admin.py          # Configuração do admin
│   ├── urls.py           # URLs do app
│   ├── fixtures/         # Dados de exemplo
│   └── templates/        # Templates HTML
├── static/               # Arquivos estáticos
│   └── images/          # Imagens (favicon, logos)
├── templates/           # Templates base
└── manage.py           # Script de gerenciamento Django
```

## 🗃️ Dados de Exemplo

O comando `loaddata dados_iniciais` carrega:

- **5 Veículos:** Diferentes modelos e placas
- **5 Motoristas:** Com nomes e CPFs fictícios
- **5 Oficinas:** Estabelecimentos variados
- **5 Serviços:** Histórico de manutenções

## 🔧 Funcionalidades

### Dashboard
- Visualização de totais de cada entidade
- Interface limpa com cards informativos

### CRUD Motoristas (Completo)
- ✅ Listar motoristas
- ✅ Criar novo motorista
- ✅ Editar motorista existente
- ✅ Visualizar detalhes
- ✅ Remover motorista

### Para os Alunos
- 🔄 CRUD de Veículos
- 🔄 CRUD de Oficinas  
- 🔄 CRUD de Serviços de Manutenção

## 🎨 Interface

- **Framework:** Bootstrap 5.3.3
- **Cores:** Verde institucional do IFRN
- **Layout:** Responsivo com sidebar lateral
- **Logo:** IFRN (colocar arquivo `ifrn.jpg` em `static/images/`)

## 📱 URLs Disponíveis

| URL | Descrição |
|-----|-----------|
| `/` | Dashboard principal |
| `/motoristas/` | Lista de motoristas |
| `/motoristas/novo/` | Criar motorista |
| `/motoristas/{id}/` | Detalhes do motorista |
| `/motoristas/{id}/editar/` | Editar motorista |
| `/motoristas/{id}/deletar/` | Remover motorista |
| `/admin/` | Painel administrativo |

## 🛠️ Comandos Úteis

### Resetar banco de dados
```powershell
python manage.py flush
python manage.py migrate
python manage.py loaddata dados_iniciais
```

### Criar novas migrações
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Coletar arquivos estáticos (produção)
```powershell
python manage.py collectstatic
```

### Verificar problemas
```powershell
python manage.py check
```

## 📝 Modelos de Dados

### Veículo
- `placa` (CharField, único)
- `modelo` (CharField)

### Motorista  
- `nome` (CharField)
- `cpf` (CharField, único)

### Oficina
- `nome` (CharField)

### ServicoManutencao
- `veiculo` (ForeignKey)
- `oficina` (ForeignKey)
- `motorista` (ForeignKey, opcional)
- `data_servico` (DateField)
- `descricao` (TextField)

## 🚧 Desenvolvimento

### Para adicionar novos CRUDs:

1. **Models:** Já estão prontos em `oficina/models.py`
2. **Views:** Criar function-based views em `oficina/views.py`
3. **URLs:** Adicionar rotas em `oficina/urls.py`
4. **Templates:** Criar em `oficina/templates/oficina/`
5. **Forms:** Adicionar em `oficina/forms.py`

### Exemplo de URL:
```python
path('veiculos/', views.veiculo_list_view, name='veiculo_list'),
```

### Exemplo de View:
```python
def veiculo_list_view(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'oficina/veiculo_list.html', {'object_list': veiculos})
```

## 🔗 Links Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/)
- [Portal IFRN](https://portal.ifrn.edu.br/)

## 📄 Licença

Projeto desenvolvido para fins educacionais - IFRN 2025

---

**Desenvolvido para o Instituto Federal do Rio Grande do Norte (IFRN)**
