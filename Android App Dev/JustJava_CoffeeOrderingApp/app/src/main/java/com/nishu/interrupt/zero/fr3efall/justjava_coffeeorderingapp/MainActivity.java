package com.nishu.interrupt.zero.fr3efall.justjava_coffeeorderingapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int quantity = 0;
    int prize = 10;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void increment(View view) {
        quantity++;
        display(quantity);

    }

    public void decrement(View view) {
        if (quantity > 0)
            quantity--;
        display(quantity);

    }

    private void display(int num) {
        TextView quantity_text_view = (TextView) findViewById(
                R.id.quantity_num);
        quantity_text_view.setText("" + num);

        TextView amount_text_view = (TextView) findViewById(
                R.id.amount);
        amount_text_view.setText("Rs. " + (quantity * prize));

    }

    public void orderClicked(View view) {

    }


}
