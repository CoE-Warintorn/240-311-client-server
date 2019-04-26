<template>
  <div class="books">
    <b-container>
      <b-row>
        <b-col cols="10">
          <h1>Books</h1>
        </b-col>
        <b-col>
          <b-button variant="success" v-b-modal.book-modal>Add Book</b-button>
        </b-col>
      </b-row>
      <!-- <hr> -->
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Author</th>
            <th scope="col">Read?</th>
            <th scope="col"></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(book, index) in books" :key="index">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>
              <span v-if="book.is_read">Yes</span>
              <span v-else>No</span>
            </td>
            <td style="width: 200px">
              <b-row>
              <b-col>
                <b-button variant="info"
                          v-b-modal.book-update-modal
                          @click="editBook(book)">
                  update
                </b-button>
              </b-col>
              <b-col>
                <b-button variant="outline-danger"
                          @click="onDeleteBook(book)">
                  delete
                </b-button>
              </b-col>

              </b-row>
            </td>
          </tr>
        </tbody>
      </table>
    </b-container>
    <!-- add -->
    <b-modal ref="addBookModal"
            id="book-modal"
            title="Add a new book"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.is_read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="success">Submit</b-button>
        <b-button type="reset" variant="outline-danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!-- update -->
    <b-modal ref="editBookModal"
            id="book-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.is_read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        anthor: '',
        is_read: [],
      },
      editForm: {
        id: '',
        title: '',
        author: '',
        is_read: [],
      },
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/api/books';
      axios.get(path)
        .then((res) => {
          // console.log('this is data');
          // console.log(res.data);
          this.books = res.data;
          // console.log(this.books)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      console.log('do get books');
    },
    addBook(payload) {
      const path = 'http://localhost:5000/api/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },
    editBook(book) {
      console.log(book)
      this.editForm = book;
      console.log("fetch data");
      console.log(this.editForm._id.$oid);
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.is_read = [];
      this.editForm._id.$oid = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.is_read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let is_read = false;
      if (this.addBookForm.is_read[0]) is_read = true;

      console.log(is_read);
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        is_read,
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let is_read = false;
      if (this.editForm.is_read[0]) is_read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        is_read
      };
      this.updateBook(payload, this.editForm._id.$oid);
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/api/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks();
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/api/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book._id.$oid);
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
