from django.test import TestCase
from .models import Livro
from django.urls import reverse
from datetime import date


# TESTES AUTOMATIZADOS ----------------------------------------------------------------

from django.test import TestCase
from django.urls import reverse
from .models import Livro
from datetime import date

class LivroTests(TestCase):
    def setUp(self):
        self.livro = Livro.objects.create(
            titulo='Livro Original',
            autor='Autor Original',
            data_publicacao=date(2024, 1, 1)
        )

    def test_criacao_livro_via_formulario(self):
        response = self.client.post(reverse('adicionar_livro'), {
            'titulo': 'Novo Livro',
            'autor': 'Novo Autor',
            'data_publicacao': '2024-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Livro.objects.count(), 2)
        livro = Livro.objects.get(titulo='Novo Livro')
        self.assertEqual(livro.autor, 'Novo Autor')
        self.assertEqual(livro.data_publicacao, date(2024, 1, 1))

    def test_listagem_livros(self):
        response = self.client.get(reverse('lista_livros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Livro Original')

    def test_atualizacao_livro_via_formulario(self):
        response = self.client.post(reverse('atualizar_livro', args=[self.livro.id]), {
            'titulo': 'Livro Atualizado',
            'autor': 'Autor Atualizado',
            'data_publicacao': '2024-01-01'
        })
        self.assertEqual(response.status_code, 302)
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, 'Livro Atualizado')
        self.assertEqual(self.livro.autor, 'Autor Atualizado')

    def test_exclusao_livro(self):
        livro_id = self.livro.id
        response = self.client.post(reverse('excluir_livro', args=[livro_id]))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Livro.DoesNotExist):
            Livro.objects.get(id=livro_id)

    def test_validacao_formulario(self):
        response = self.client.post(reverse('adicionar_livro'), {
            'titulo': '',
            'autor': 'Autor',
            'data_publicacao': '2024-01-01'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este campo é obrigatório.')


# TESTES UNITÁRIOS -----------------------------------------------------------------

class LivroModelTest(TestCase):
    def setUp(self):
        self.livro = Livro.objects.create(
            titulo="Livro de Teste",
            autor="Autor de Teste",
            data_publicacao=date(2024, 6, 11)
        )

    def test_criacao_livro(self):
        """Testa se o livro foi criado corretamente"""
        self.assertEqual(self.livro.titulo, "Livro de Teste")
        self.assertEqual(self.livro.autor, "Autor de Teste")
        self.assertEqual(self.livro.data_publicacao, date(2024, 6, 11))
        

        """Ex.: Teste Incorreto
        self.assertEqual(self.livro.titulo, "Livro Errado")
        self.assertEqual(self.livro.autor, "Autor Errado")
        self.assertEqual(self.livro.data_publicacao, date(2024, 1, 1))
        """

    def test_metodo_str(self):
        """Testa o método __str__ do modelo"""
        self.assertEqual(str(self.livro), "Livro de Teste")

        """Testa o método __str__ do modelo
        self.assertEqual(str(self.livro), "Livro Errado")
        """


    def test_atualizacao_livro(self):
        """Testa a atualização de um livro"""
        self.livro.titulo = "Livro Atualizado"
        self.livro.save()
        self.assertEqual(self.livro.titulo, "Livro Atualizado")

        """Ex.: Teste Incorreto
        self.livro.titulo = "Livro Não atualizacao"
        self.livro.save()
        self.assertEqual(self.livro.titulo, "Livro Não Atualizado")
        """

    def test_exclusao_livro(self):
        """Testa a exclusão de um livro"""
        livro_id = self.livro.id
        self.livro.delete()
        with self.assertRaises(Livro.DoesNotExist):
            Livro.objects.get(id=livro_id)

        

    def test_contagem_livros(self):
        """Testa a contagem de livros no banco de dados"""
        self.assertEqual(Livro.objects.count(), 1)
        Livro.objects.create(
            titulo="Outro Livro",
            autor="Outro Autor",
            data_publicacao=date(2024, 6, 11)
        )
        self.assertEqual(Livro.objects.count(), 2)
    