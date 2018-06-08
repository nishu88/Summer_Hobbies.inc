package com.nishu.interrupt.zero.fr3efall.justjava_coffeeorderingapp;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    int quantity = 0;
    int prize = 45;
    String emailAddress[]={"nishud3301@gmail.com"};



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        nextpage();
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
        TextView amt_text_view=(TextView) findViewById(
                R.id.bill);
        EditText personName=(EditText) findViewById(
                R.id.name);
        String order="Name: "+personName.getText().toString()+" \n";
        order=order+"Quantity: "+quantity;
        amt_text_view.setText(order);

        TextView thankYou_text_view=(TextView) findViewById(
                R.id.thankYou);
        thankYou_text_view.setText("Thank you, Visit Again!!!");

        Button but=(Button) findViewById(
                R.id.order_button);
        but.setText("Order Complete");

        composeEmail(emailAddress,"Coffee order for Mr/Ms. "+personName.getText().toString(),order);


    }


    public void composeEmail(String[] addresses, String subject,String summary) {
        Intent intent = new Intent(Intent.ACTION_SENDTO);
        intent.setData(Uri.parse("mailto:")); // only email apps should handle this
        intent.putExtra(Intent.EXTRA_EMAIL, addresses);
        intent.putExtra(Intent.EXTRA_SUBJECT, subject);
        intent.putExtra(Intent.EXTRA_TEXT,summary);
        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);
        }
    }

    public void nextpage(){
        Button button=(Button) findViewById(R.id.next);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this,SecondActitvity.class));
            }
        });
    }


}
