# Instruções Rápidas para Executar o Projeto

## Windows - Passo a Passo

1. **Baixar o projeto e navegar para a pasta:**
   ```powershell
   cd oficina-mecanica
   ```

2. **Criar ambiente virtual:**
   ```powershell
   python -m venv venv
   ```

3. **Ativar ambiente virtual:**
   ```powershell
   .\venv\Scripts\activate
   ```

4. **Instalar dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

5. **Configurar banco de dados:**
   ```powershell
   python manage.py migrate
   ```

6. **Carregar dados de exemplo:**
   ```powershell
   python manage.py loaddata dados_iniciais
   ```

7. **Criar superusuário (opcional):**
   ```powershell
   python manage.py createsuperuser
   ```

8. **Executar servidor:**
   ```powershell
   python manage.py runserver
   ```

9. **Acessar:** http://127.0.0.1:8000/

## Dados Carregados:
- 5 Veículos
- 5 Motoristas  
- 5 Oficinas
- 5 Serviços de Manutenção

## CRUD Pronto:
- ✅ Motoristas (completo)
- 🔄 Veículos (para alunos)
- 🔄 Oficinas (para alunos)
- 🔄 Serviços (para alunos)
