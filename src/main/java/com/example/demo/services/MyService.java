package com.example.demo.services;

import com.example.demo.dtos.TriangleTops;
import org.springframework.stereotype.Service;

@Service
public class MyService {
    public double areaTriangle(TriangleTops triangleTops) {
        return 0.5 * Math.abs((triangleTops.getX1() - triangleTops.getX3()) * (triangleTops.getY2() - triangleTops.getY3()) - (triangleTops.getX2() - triangleTops.getX3()) * (triangleTops.getY1() - triangleTops.getY3()));
    }
}
