package com.example.dermato;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class hompg extends AppCompatActivity {
    Button b1,b2,b3,b4,b5,b6,b7;
    SharedPreferences sh;
    TextView t1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hompg);

        b1=findViewById(R.id.button8);
        b2=findViewById(R.id.button9);
        b3=findViewById(R.id.button10);
        b4=findViewById(R.id.button11);
        b5=findViewById(R.id.button12);
        b6=findViewById(R.id.button13);
        b7=findViewById(R.id.button7);

        t1 = findViewById(R.id.textView17);

        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        t1.setText("hi there "+sh.getString("username",""));

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),viewprofile.class);
                startActivity(ii);


            }
        });

        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent ii=new Intent(getApplicationContext(),viewdoctor.class);
                startActivity(ii);

            }
        });
        b3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });
        b4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),sendfeedback.class);
                startActivity(ii);

            }
        });
        b5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(),Viewbooking.class);
                startActivity(ii);


            }
        });
        b6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(), MainActivity2login.class);
                startActivity(ii);

            }
        });
        b7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent ii=new Intent(getApplicationContext(), chatdoctor.class);
                startActivity(ii);

            }

    });
}
}