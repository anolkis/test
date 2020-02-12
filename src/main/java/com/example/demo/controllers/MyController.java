package com.example.demo.controllers;

import com.example.demo.dtos.TriangleTops;
import com.example.demo.services.MyService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequiredArgsConstructor
@RestController
@RequestMapping("api")
public class MyController {

    private final MyService myService;
/*
    {
		"x1" : 0,
		"y1" : 0,
		"x2" : 0,
		"y2" : 1,
		"x3" : 1,
		"y3" : 0
	}
*/
    @PostMapping("area-triangle")
    public double areaTriangle(@RequestBody TriangleTops triangleTops) {
        return myService.areaTriangle(triangleTops);
    }
}
